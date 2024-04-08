#creo una classe chiamata ristorante con un valore descrizione uguale a 0 collegato ad un successivo metodo "aggiungi descrizione"
#un dizionario vuoto che rappresenta il menu
#definisco un metodo init con nome e tipo di cucina e il parametro aperto=False

#metodi della classe:
#aggiungi_descrizione, che chiede input di descrivere il ristorante e imposta il contatore a 1
#descrivi_ristorante dove if contatore = 0 printa "devi prima aggiungere una descrizione", se è uguale a 1, stampa aggiungi descrizione
#stato_apertura stampa semplicemente il valore del parametro apertura
#apri_ristorante e chiudi_ristorante
#aggiungi_al_menu dove imposto un valore


class ristorante:
    contatore_descrizione = 0
    menu = {'primi_piatti': {"portata": {'nome':"" ,'prezzo': ""}},"secondi_piatti": {"portata": {'nome':"",'prezzo': ""}},"frutta":{"portata":{'nome':"",'prezzo': ""}}, "dolce": {"portata":{'nome':"",'prezzo': ""}}}
    descrizione_ristorante = ""

    #definisco i metodi
    #metodo costruttore
    def __init__(self, nome, tipo_di_cucina, aperto=False):
        self.nome= nome
        self.tipo_di_cucina = tipo_di_cucina
        self.aperto = aperto
    
    #metodo aggiungi descrizione
    def aggiungi_descrizione(self, descrizione= input("Inserisci una descrizione")):
        if ristorante.contatore_descrizione == 0:
             ristorante.descrizione_ristorante = descrizione
        if ristorante.contatore_descrizione == 1:
            print("La descrizione è già stata aggiunta")
    
    #aggiungo il metodo descrivi ristorante
    def descrivi_ristorante(self):
        return print(ristorante.descrizione_ristorante)
    
    #metodo stato apertura
    def stato_apertura(self):
        print(self.aperto)

    #metodo apri ristorante
    def apri_ristorante(self):
        self.aperto=True
    
    #metodo chiudi ristorante
    def chiudi_ristorante(self):
        self.aperto=False
    
    #metodo aggiungi al menu
    def aggiungi_al_menu(self, quale_piatto, portata, nome, prezzo):
        if portata in ristorante.menu['primi_piatti']:
            ristorante.menu[quale_piatto][portata]['prezzo'] += prezzo
        else:
            ristorante.menu[quale_piatto][portata] = {'nome': nome, 'prezzo': prezzo}
        print(f"Aggiunto: {portata}, nome: {nome}, Prezzo: {prezzo}")

    #metodo togli dal menu
    def togli_dal_menu (self, quale_piatto, portata):
        del ristorante.menu[quale_piatto][portata]

    #stampa menu
    def stampa_menu(self):
        return print(ristorante.menu)
    

#test della classe




        
