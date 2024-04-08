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
    menu = {'primi_piatti': {"1": {'nome':"" ,'prezzo': ""}},"secondi_piatti": {"1": {'nome':"",'prezzo': ""}},"frutta":{"1":{'nome':"",'prezzo': ""}}, "dolce": {"1":{'nome':"",'prezzo': ""}}}
    descrizione_ristorante = ""

    #definisco i metodi
    #metodo costruttore
    def __init__(self, nome, tipo_di_cucina, aperto=False):
        self.nome= nome
        self.tipo_di_cucina = tipo_di_cucina
        self.aperto = aperto
    
    #metodo aggiungi descrizione
    def aggiungi_descrizione(self, descrizione= input("Inserisci una descrizione\n")):
        if ristorante.contatore_descrizione == 0:
             ristorante.descrizione_ristorante = descrizione
        if ristorante.contatore_descrizione == 1:
            print("La descrizione è già stata aggiunta")
    
    #aggiungo il metodo descrivi ristorante
    def descrivi_ristorante(self):
        return print(ristorante.descrizione_ristorante)
    
    #metodo stato apertura
    def stato_apertura(self):
        if self.aperto==True:
            print("Il ristorante è aperto")
        elif self.aperto==False:
            print("Il ristorante è chiuso")

    #metodo apri ristorante
    def apri_ristorante(self):
        self.aperto=True
        
    #metodo chiudi ristorante
    def chiudi_ristorante(self):
        self.aperto=False
    
    #metodo aggiungi al menu
    def aggiungi_al_menu(self, quale_piatto, n_portata, nome, prezzo):
        if portata in ristorante.menu['primi_piatti']:
            ristorante.menu[quale_piatto][n_portata]['prezzo'] += prezzo
        else:
            ristorante.menu[quale_piatto][n_portata] = {'nome': nome, 'prezzo': prezzo}
        print(f"Aggiunto: nome: {nome}, Prezzo: {prezzo}")

    #metodo togli dal menu
    def togli_dal_menu (self, quale_piatto, n_portata):
        del ristorante.menu[quale_piatto][n_portata]

    #stampa menu
    def stampa_menu(self):
        return print(ristorante.menu)
    

#test della classe

while True:
    print("benvenuto sul gestore di creazione ristorante")
    nome = input("digita il nome del tuo ristorante")
    tipo_cucina = input("digita il tipo di cucina del tuo ristorante")
    ristorante_creato = ristorante(nome, tipo_cucina)
    print("Benvenuto, aggiungi al menu e in seguito siamo pronti per aprire un ristorante")
    tipo_di_piatto


        
