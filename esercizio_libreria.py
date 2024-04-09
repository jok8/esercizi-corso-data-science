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
    
    def cerca_libro(self,Libro):
        if Libro in Libreria.catalogo:
            print(f"{Libro} è presente nel catalogo")
    
    def mostra_catalogo(self):
        print(Libreria.catalogo)


while True:
    aggiunta_libro = input("vuoi aggiungere un libro?")
    if aggiunta_libro == "sì":
        nome_libro = input("Aggiungi un nome")
        autore_libro = input("Aggiungi l'autore")
        ISBN_libro = input("Aggiungi ISBN")
        libro_aggiunto = Libreria(nome_libro, autore_libro, ISBN_libro)
        libro_aggiunto.aggiungi_libro(nome_libro, autore_libro, ISBN_libro)
    else:
        print("ok, allora non aggiungiamo nulla")
        input("cosa vuoi fare?")
        
