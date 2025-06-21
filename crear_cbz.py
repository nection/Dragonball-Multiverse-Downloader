import os
import re
import requests
import zipfile
import shutil
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def sanitize_filename(name):
	"""Limpia un string para que sea un nombre de archivo válido."""
	name = re.sub(r'^Capítulo\s*\d+\s*:?\s*', '', name, flags=re.IGNORECASE).strip()
	name = re.sub(r'[\\/*?:"<>|]', "", name)
	name = re.sub(r'\s+', '_', name)
	return name

def create_cbz_from_folder(folder_path, cbz_path):
	"""Crea un archivo CBZ a partir de las imágenes de una carpeta, ordenadas."""
	images = sorted(os.listdir(folder_path))
	with zipfile.ZipFile(cbz_path, 'w', zipfile.ZIP_DEFLATED) as zf:
		for image in images:
			image_path = os.path.join(folder_path, image)
			zf.write(image_path, arcname=image)

def download_manga_definitivo():
	"""
	Versión final que gestiona los 'Referer' y busca la imagen de forma robusta.
	"""
	base_url = "https://www.dragonball-multiverse.com/es/"
	chapters_url = "https://www.dragonball-multiverse.com/es/chapters.html?comic=page"
	main_download_folder = "dragonball_multiverse_cbz"
	temp_folder = os.path.join(main_download_folder, "temp_download")

	if not os.path.exists(main_download_folder):
		os.makedirs(main_download_folder)
		print(f"Carpeta principal '{main_download_folder}' creada.")

	with requests.Session() as session:
		session.headers.update({
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
		})

		try:
			print("Accediendo a la página de capítulos...")
			response = session.get(chapters_url)
			response.raise_for_status()
			soup = BeautifulSoup(response.content, 'html.parser')

			chapter_divs = soup.find_all('div', class_='chapter')
			if not chapter_divs:
				print("ERROR: No se encontraron los bloques de capítulos.")
				return

			print(f"Se encontraron {len(chapter_divs)} capítulos.")

			for i, chapter_div in enumerate(chapter_divs):
				chapter_title_tag = chapter_div.find('h4')
				if not chapter_title_tag: continue

				raw_title = chapter_title_tag.text.strip()
				cbz_filename = f"Capitulo_{str(i + 1).zfill(2)}_{sanitize_filename(raw_title)}.cbz"
				cbz_path = os.path.join(main_download_folder, cbz_filename)

				if os.path.exists(cbz_path):
					print(f"\nEl archivo '{cbz_filename}' ya existe. Saltando.")
					continue
				
				print(f"\nProcesando: {raw_title}")

				page_links = {urljoin(base_url, a['href']) for a in chapter_div.find_all('a', href=re.compile(r'page-\d+\.html'))}
				if not page_links:
					print(f"  Advertencia: No se encontraron páginas para '{raw_title}'.")
					continue
				
				sorted_pages = sorted(list(page_links))
				total_pages = len(sorted_pages)

				if os.path.exists(temp_folder): shutil.rmtree(temp_folder)
				os.makedirs(temp_folder)

				for j, page_url in enumerate(sorted_pages):
					img_name = f"{str(j+1).zfill(3)}.jpg"
					img_path = os.path.join(temp_folder, img_name)
					
					try:
						print(f"  Descargando página {j+1}/{total_pages}...")
						
						session.headers.update({'Referer': chapters_url})
						page_response = session.get(page_url, timeout=15)
						page_response.raise_for_status()
						
						page_soup = BeautifulSoup(page_response.content, 'html.parser')
						
						# --- BÚSQUEDA ROBUSTA DE LA IMAGEN (LA CLAVE DEL ARREGLO) ---
						# Busca cualquier <img> cuya dirección (src) contenga 'image.php'
						img_tag = page_soup.find('img', src=re.compile(r'image\.php'))
						
						if img_tag and 'src' in img_tag.attrs:
							img_url = urljoin(page_url, img_tag['src'])
							
							session.headers.update({'Referer': page_url})
							img_response = session.get(img_url, timeout=30)
							img_response.raise_for_status()
							
							with open(img_path, 'wb') as f:
								f.write(img_response.content)
						else:
							print(f"  ERROR: No se encontró la etiqueta de imagen en {page_url}")

					except requests.exceptions.RequestException as e:
						print(f"  Error de red al procesar {page_url}: {e}")

				if os.listdir(temp_folder):
					print(f"Creando archivo '{cbz_filename}'...")
					create_cbz_from_folder(temp_folder, cbz_path)
					print(f"'{cbz_filename}' creado con éxito.")
				else:
					print(f"No se descargaron imágenes para '{raw_title}', no se creará el CBZ.")

				shutil.rmtree(temp_folder)

			print("\n\n¡PROCESO COMPLETADO!")
			print(f"Todos los archivos han sido guardados en la carpeta: '{main_download_folder}'")

		except requests.exceptions.RequestException as e:
			print(f"Error crítico: {e}")
		finally:
			if os.path.exists(temp_folder):
				shutil.rmtree(temp_folder)

if __name__ == "__main__":
	download_manga_definitivo()