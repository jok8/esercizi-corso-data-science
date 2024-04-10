# creo la classe padre registro vendite
#     creo un dizionario che verrà compilato dall'oggetto della classe figlia
#     creo un metodo che calcola la somma con un for loop
#     creo un metodo che calcoli la media basandosi sul metodo della somma
#     creo un metodo che trovi in dictionary tutte le vendite al di sopra della media con un for loop
# creo la classe figlia giorno di vendita con 1, 2, 3, 30
#     creo un metodo che aggiunga i dati al dizionario dove chiede se vuole inserire i valori con un while
#         creo un try e except all'interno per gestire valueerror quando:
#                             - l'utente inserisce una lettera al posto di un numero/ il numero non è int
#                             - il numero è minore di 0




class registro_vendite:
    registro = {}
    
    #metodo costruttore
    def __init__(self, anno):
        self.anno = anno

    #metodo della somma dei giorni di un mese
    def somma_giorni(self, mese):
        if mese in registro_vendite:
            count= 0
            sum = 0
            for key in registro_vendite[mese]:
                count+=1
                sum+=registro_vendite[mese][key]
            print("questa è la somma delle vendite del mese")
        else:
            print("mese non ancora registrato")
    
    #metodo della media dei giorni
    def media_dei_giorni(self, mese):
        if mese in registro_vendite:
            count= 0
            sum = 0
            for key in registro_vendite[mese]:
                count+=1
                sum+=registro_vendite[mese][key]
            print(f"questa è la media delle vendite del mese: {sum/count}")
        else:
            print("mese non ancora registrato")
    
    #metodo del giorno più alto della media
    def superiore_alla_media(self, mese):
        if mese in registro_vendite:
            for giorno in registro_vendite[mese]:
                if giorno > self.media_dei_giorni():
                    print(f"Il giorno {giorno} è superiore alla media")
        else:
            print("mese non ancora registrato")


class giorno_di_vendita(registro_vendite):
    #metodo costruttore
    def __init__(self, mese, giorno, anno):
        super().__init__(anno)
        self.mese = mese
        self.giorno = giorno

    def aggiungi_a_registro(self, vendite):
        self.vendite = vendite
        self.registro[self.mese]={self.giorno : self.vendite}



flag = True
while True:
    dati = int(input("Benvenuto nell'area vendite, per inserire dei dati scrivi 1, per chiudere l'applicazione scrivi 0"))
    if dati == 1:
        registrazione_mese = input("Perfetto, inserisci il mese in cui inserire i dati")
        if registrazione_mese not in registro_vendite.registro:
            try:
               registrazione_giorno = int(input("dimmi il numero del giorno che vuoi inserire"))
            except ValueError:
                print("devi inserire un numero")
            registrazione_vendite = int(input("inserisci un valore per le vendite"))
            oggetto_giorno = giorno_di_vendita(registrazione_mese,registrazione_giorno,registrazione_vendite)
            conferma = int(input("Pe confermare scrivere 1\n Per uscire scrivere 0"))
            if conferma == 1:
                oggetto_giorno.aggiungi_a_registro
                print("Perfetto, vendita aggiunta")
                altra_aggiunta = int(input("per continuare ad aggiungere vendite, scrivere 1, per stampare la media delle vendite del mese scrivere 2"))
                if altra_aggiunta == 1:
                    continue
                elif altra_aggiunta == 2:
                    oggetto_giorno.media_dei_giorni
            elif conferma == 0:
                print("conferma non selezionata, uscita dal programma")
                break
        


