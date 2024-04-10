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
    def __init__(self)
        pass

    #metodo della somma dei giorni di un mese
    def somma_giorni(self, mese):
        if mese in registro_vendite:
            count= 0
            sum = 0
            for key in registro_vendite[mese]
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
            for key in registro_vendite[mese]
                count+=1
                sum+=registro_vendite[mese][key]
            print(f"questa è la media delle vendite del mese: {sum/count}")
        else:
            print("mese non ancora registrato")
    
    #metodo del giorno più alto della media
    def superiore_alla_media(self, mese):
        if mese in registro_vendite:
            for giorno in registro_vendite[mese]
                if giorno > self.media_dei_giorni():
                    print(f"Il giorno {giorno} è superiore alla media")
        else:
            print("mese non ancora registrato")


class giorno_di_vendita(registro_vendite):
    #metodo costruttore
    def __init__(self, mese, giorno):
        self.mese = mese
        self.giorno = giorno


flag = True
while True:
    dati = input("Benvenuto nell'area vendite, per inserire dei dati scrivi 1, per chiudere l'applicazione scrivi 0")
    if dati == 1:
        registrazione_mese = input("Perfetto, inserisci il mese in cui inserire i dati")
        if registrazione_mese not in registro_vendite.registro:
            registrazione_giorno = 
            registro_vendite.registro.setdefault(registrazione_mese,)
        


