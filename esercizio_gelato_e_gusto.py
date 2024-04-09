#inizio definendo una classe padre gelato con mostra dettagli

class Gelato:
    def __init__(self):
        pass

    def mostra_dettagli(self):
        print("Sono un gelato al")

#definisco una classe figlia gusto
class Gusto(Gelato):
    #inizializzo un array vuoto gusti che andrò poi a riempire con i parametri dell'init
    gusti = ["","",""]

    def __init__(self, gusto1, gusto2, gusto3):
        super().__init__()
        Gusto.gusti[0] = gusto1
        Gusto.gusti[1] = gusto2
        Gusto.gusti[2] = gusto3
        
    #definisco un metodo che stampi i dettagli della classe padre oltre ai gusti
    def mostra_dettagli(self):
        super().mostra_dettagli() 
        print(self.gusti[0])
        print(self.gusti[1])
        print(self.gusti[2])

#definisco un contatore che parte da 0    
contatore = 0

#finchè il contatore è minore uguale a 3, fa partire il loop
while contatore<=3:
    #chiedo se vuole fare un gelato
    domanda = input("Vuoi fare un gelato?\n")
    if domanda == "sì":
        #se la risposta è sì, chiederà il primo gusto e aumenterà il contatore di 1
        primo_gusto = input("scegli il primo gusto\n")
        contatore += 1
        #chiederà il secondo gusto e aumenterà il contatore di 1
        secondo_gusto = input("scegli il secondo gusto\n")
        contatore += 1
        #chiederà il terzo gusto e aumenterà il contatore di 1
        terzo_gusto = input("scegli il terzo gusto\n")
        contatore += 1
        #creo un oggetto gelato che riprende la classe gusto e ha come parametri i gusti
        gelato = Gusto(primo_gusto, secondo_gusto, terzo_gusto)
        #stampa i dettagli del gelato creato
        gelato.mostra_dettagli()
    #se non vuole fare un gelato, farà un print e uscirà dal ciclo
    else:
        print("ok niente gelato :(")
        break


