# Descarregador de Bola de Drac Multiverse en CBZ

Aquest script en Python permet descarregar tots els capítols del webcòmic *Bola de Drac Multiverse* des de la seva pàgina oficial en espanyol i els empaqueta automàticament en fitxers `.cbz` per a una lectura còmoda en qualsevol visor de còmics.

## Característiques

*   **Descàrrega automatitzada**: Obté tots els capítols i pàgines disponibles des de l'índex principal.
*   **Organització per capítols**: Cada capítol es desa en el seu propi fitxer `.cbz`.
*   **Creació de fitxers CBZ**: Comprimeix les imatges de cada capítol en un arxiu `.cbz`, el format estàndard per a còmics digitals.
*   **Nomenclatura intel·ligent**: Anomena els fitxers de manera ordenada (`Capítol_01_Títol.cbz`, `Capítol_02_Títol.cbz`...).
*   **Eficient**: Si ja has descarregat un capítol prèviament, l'script el saltarà per no tornar-lo a descarregar.

## Requisits Previs

-   **Python 3**: Necessites tenir Python 3 instal·lat al teu sistema. Per verificar si el tens, obre una terminal i executa:
    ```bash
    python3 --version
    ```
    Si no el tens, pots descarregar-lo des de [python.org](https://www.python.org/downloads/) o instal·lar-lo a través d'un gestor de paquets com Homebrew a macOS (`brew install python`).

## Instruccions d'Instal·lació i Ús

Segueix aquests passos detallats per engegar l'script al teu ordinador (instruccions optimitzades per a macOS i Linux).

### Pas 1: Clonar o Descarregar el Repositori

Obre una terminal i clona el repositori de GitHub:

```bash
git clone https://github.com/el-teu-usuari/el-teu-repositori.git
```
O, si ho prefereixes, descarrega el fitxer ZIP des de GitHub i descomprimeix-lo en una carpeta de la teva elecció.

### Pas 2: Navegar a la Carpeta del Projecte
Fes servir la comanda `cd` per entrar a la carpeta que acabes de clonar o descomprimir.
```bash
cd el-teu-repositori
```

### Pas 3: Crear un Entorn Virtual
És una pràctica recomanada i essencial crear un entorn virtual per instal·lar les dependències del projecte de forma aïllada, evitant conflictes amb els paquets del teu sistema.
```bash
python3 -m venv venv
```
Aquesta comanda crearà una carpeta anomenada `venv` dins del teu projecte.

### Pas 4: Activar l'Entorn Virtual
Per començar a utilitzar l'entorn, necessites activar-lo.
```bash
source venv/bin/activate
```
Notaràs que l'inici de la línia de comandes de la teva terminal canvia, mostrant `(venv)` al principi. Això indica que l'entorn virtual està actiu.

### Pas 5: Instal·lar les Dependències
Amb l'entorn ja actiu, instal·la les llibreries necessàries (`requests` i `beautifulsoup4`) fent servir el gestor de paquets `pip`.
```bash
pip install requests beautifulsoup4
```
Això instal·larà les llibreries únicament dins del teu entorn virtual, sense afectar el sistema global.

### Pas 6: Executar l'Script
Ja està tot a punt! Ara només has d'executar l'script principal:
```bash
python3 crear_cbz.py
```
L'script començarà a treballar. Veuràs missatges a la terminal indicant el progrés: quin capítol està processant, quina pàgina està descarregant i quan es crea cada fitxer `.cbz`.

### Pas 7: A gaudir!
Un cop l'script acabi, trobaràs una nova carpeta anomenada `dragonball_multiverse_cbz` al directori del projecte. Dins hi haurà tots els còmics en format `.cbz`, llestos per ser transferits al teu lector de còmics preferit.

---
### Per a Usuaris de Windows
Els passos són pràcticament els mateixos, però les comandes per activar l'entorn virtual varien:

*   **Crear entorn:** `python -m venv venv`
*   **Activar entorn:** `.\venv\Scripts\activate`
*   **Instal·lar dependències:** `pip install requests beautifulsoup4`
*   **Executar script:** `python crear_cbz.py`

---

## Notes Addicionals
*   **Desactivar l'entorn virtual**: Quan hagis acabat de fer servir l'script, pots desactivar l'entorn simplement escrivint `deactivate` a la terminal.
*   **Errors de xarxa**: Si l'script falla per un problema de connexió, pots tornar-lo a executar. Gràcies a la comprovació de fitxers existents, continuarà on s'havia quedat.

## Avís Legal
Aquest script ha estat creat amb finalitats educatives i per a ús personal. El contingut descarregat pertany als seus respectius autors i propietaris de drets d'autor (Salagir i Gogeta Jr./Asura). Si us plau, dona suport a l'obra original visitant la seva pàgina web oficial. Utilitza aquesta eina de forma responsable.
