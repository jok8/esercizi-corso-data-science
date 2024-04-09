#faccio una classe madre libreria con attributo catalogo
    #metodi aggiungi libro, rimuovi libro, cerca per titolo, mostra catalogo

#faccio una classe figlia libro che accetta attributi titolo, autore e isbn
    #metodi descrizione, che descrive il libro usando tutti e tre gli attributi




class Libro:
    def __init__ (self, titolo, autore, ISBN):
        self.titolo = titolo
        self.autore = autore
        self.ISBN = ISBN
    

class Libreria(Libro):
    catalogo = {}
    def __init__ (self, titolo, autore, ISBN):
        super().__init__(titolo, autore, ISBN)
    
    def aggiungi_libro(self, titolo, autore, ISBN):
        super().__init__(titolo, autore, ISBN)
        if ISBN in Libreria.catalogo:
            print("Libro già presente nel catalogo")
        else:
            Libreria.catalogo[titolo] = {"Autore": autore, "ISBN": ISBN}

    def rimuovi_libro(self, titolo, ISBN):
        del Libreria.catalogo[titolo][ISBN]
    
    def cerca_libro(Libro):
        if Libro in Libreria.catalogo:
            print(f"{Libro} è presente nel catalogo")
    
    def mostra_catalogo():
        print(Libreria.catalogo)


while True:
    aggiunta_libro = input("vuoi aggiungere un libro?\n")
    if aggiunta_libro == "sì":
        nome_libro = input("Aggiungi un nome\n")
        autore_libro = input("Aggiungi l'autore\n")
        ISBN_libro = input("Aggiungi ISBN\n")
        libro_aggiunto = Libreria(nome_libro, autore_libro, ISBN_libro)
        libro_aggiunto.aggiungi_libro(nome_libro, autore_libro, ISBN_libro)
    else:
        print("ok, allora non aggiungiamo nulla")
        cosa_fare = int(input("cosa vuoi fare?\nScrivi:\n0 per rimuovere un libro\n1 per cercare un libro\n2 per mostrare il catalogo\n3 per uscire\n"))
        if cosa_fare == 0:
            libro_da_rimuovere = input("che libro vuoi rimuovere?\n")
            Libreria.rimuovi_libro(libro_da_rimuovere)
        elif cosa_fare == 1:
            libro_da_cercare = input("che libro vuoi cercare?\n")
            Libreria.cerca_libro(libro_da_cercare)
        elif cosa_fare == 2:
            print("Il catalogo è questo")
            Libreria.mostra_catalogo()
        elif cosa_fare == 3:
            print("uscita selezionata, arrivederci")
            break
        else:
            print("nessuna azione selezionata, arrivederci")
            break

