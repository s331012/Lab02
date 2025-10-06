import csv

def carica_da_file(file_path):
    """Carica i libri dal file"""
    biblioteca = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader =csv.reader(file,delimiter=",")
        indicesezione= 0
        numerosezioni= 0
        biblioteca= [[ for _ in range(numerosezioni)]
        for row in reader:
            titolo = row[0]
            autore = row[1]
            anno = row[2]
            pagine = row[3]
            sezione = row[4]
            biblioteca.append([titolo,autore,int(anno),int(pagine),int(sezione)])
        return biblioteca

def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    indicesezione= sezione -1
    numerosezioni= len(biblioteca)
    libro = [
    titolo.strip(),
    autore.strip(),
    int(anno),
    int(pagine),
    int(sezione),]
    biblioteca[indicesezione].append(libro)
    try:
        with open(file_path, "a", newline=' ',encoding="utf-8") as file:
            writer = csv.writer(file)
            rigadascrivere=[
                libro[0],
                libro[1],
                str(libro[2]),
                str(libro[3]),
                str(libro[4]),
            ]
            writer.writerow(rigadascrivere)

if 0 <= indicesezione < numerosezioni:
    libro = [titolo, autore, anno, pagine, sezione]
    biblioteca[indicesezione].append(libro)

def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    titolocercato=titolocercato.strip().lower()
    if libro(titolo).strip().lower()==titolocercato:
    titolo, autore, anno, pagine, sezione = libro
    return f"{titolo}, {autore}, {anno}, {pagine}, {sezione}"


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    indicesezione= sezione -1
    if not (0 <= indicesezione < len(biblioteca)):
       return False
    sezione= biblioteca[indicesezione]
    titoli = [libro[titolo] for titolo in sezione]
    return titoli

def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

