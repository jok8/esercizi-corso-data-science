dati_utente = False

while dati_utente == False:
    if input("Scrivi registrami per registrarti\n")=="registrami":
        dati_utente = [input("Inserisci uno username\n"),input("Inserisci una password\n"), input("Qual è il tuo animale preferito?\n")]

while bool(dati_utente) == True:
    if input("Scrivi accedi per accedere\n")== "accedi":
        nome_utente = input("Inserisci un nome utente\n")
        password = input("Inserisci una password\n")
        if nome_utente==dati_utente[0] and password == dati_utente[1]:
            animale_preferito = input("Benvenuto, abbiamo bisogno di un'ultima cosa:\nQual è il tuo animale preferito?\n")
            if animale_preferito==dati_utente[2]:
                print("Perfetto, andiamo")
                cosa_vuoi_fare = input("Scrivi cambia username per cambiare username, cambia password per cambiare password o logout per uscire\n")
                if cosa_vuoi_fare == "logout":
                    break
                elif cosa_vuoi_fare == "cambia username":
                    nuovo_username = input("digita nuovo username")
                    dati_utente[0]= nuovo_username
                elif cosa_vuoi_fare == "cambia password":
                    nuova_password = input("digita nuova password")
                    dati_utente[1]= nuova_password
            elif animale_preferito != dati_utente[2]:
                print("Risposta errata")
                break
        elif nome_utente != dati_utente[0]:
            print("nome utente errato")
        elif password != dati_utente[1]:
            print("password errata")
    else:
        input("Scrivi accedi per accedere\n")