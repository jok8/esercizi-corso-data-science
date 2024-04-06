# Definizione dell'inventario
inventario = {
    'penna': {'prezzo': 1.50, 'quantità': 100},
    'quaderno': {'prezzo': 2.50, 'quantità': 50},
    'zaino': {'prezzo': 25.00, 'quantità': 20}
}

def visualizza_inventario():
    for articolo, dettagli in inventario.items():
        print(f"Articolo: {articolo}, Prezzo: {dettagli['prezzo']}€, Quantità: {dettagli['quantità']}")


def aggiungi_al_inventario(articolo, prezzo, quantità):
    if articolo in inventario:
        inventario[articolo]['Quantità'] += quantità
    else:
        inventario[articolo] = {'prezzo': prezzo, 'quantità': quantità}
    print(f"Aggiunto: {articolo}, Prezzo: {prezzo}€, Quantità: {quantità}")


#definisco a priori gli amministratori
amministratore1 = {"Nome": "Carlo", "Cognome": "Rossi", "Nome utente": "Carletto", "Password": "ciao"}
amministratore2 = {"Nome": "Pippo", "Cognome": "Bianchi", "Nome utente": "Pippo1234", "Password": "hello"}
amministratore3 = {"Nome": "Caio", "Cognome": "Verdi", "Nome utente": "CaioVerdi", "Password": "comeva"}

#faccio il check se un amministratore è presente nel sistema
if some_key in amministratore1:
    print("ok")



#ti chiede l'accesso e successivamente verifica se sei un amministratore o un cliente
if input("Scrivi accedi per accedere\n")== "accedi":
        chi_accede = int(input("Scrivi 1 per accedere come un amministratore, oppure 2 per accedere come utente"))
        #parte dell'amministratore
        while bool(chi_accede) == True:
            if chi_accede==0:
                nome_utente = input("Inserisci un nome utente\n")
                if nome_utente in amministratore1.values():
                    #check password
                    password = input("Inserisci una password\n")
                    if password in amministratore1.get("Password"):
                        print("ok sei dentro")
                    else:
                        print("password errata")
                        break
                elif nome_utente in amministratore2.values():
                    #check password
                    password = input("Inserisci una password\n")
                    if password in amministratore2.get("Password"):
                        print("ok sei dentro")
                    else:
                        print("password errata")
                        break
                elif nome_utente in amministratore3.values():
                    #check password
                    password = input("Inserisci una password\n")
                    if password in amministratore3.get("Password"):
                        print("ok sei dentro")
                    else:
                        print("password errata")
                        break
                else:
                    print("nome_utente_errato")
                    break
                cosa_vuoi_fare = int(input("Cosa vuoi fare?\n Digita:\n1 per visualizzare inventario\n2 per aggiungere nuovi articoli all'inventario\n3 per visualizzare un rapporto delle vendite\n4per visualizzare i guadagni totali"))
                if cosa_vuoi_fare ==1:
                     visualizza_inventario()




            elif chi_accede==1:
                #inizializzo i dati utente come false, in quanto non si è mai registrato
                dati_utente = False
                while dati_utente == False:
                    if input("Scrivi registrami per registrarti\n")=="registrami":
                        dati_utente = [input("Inserisci uno username\n"),input("Inserisci una password\n"), input("Qual è il tuo animale preferito?\n")]
                while bool(dati_utente) == True:
                        #parte del cliente
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







        '''
        definisco un inventario
        creo un sistema di login che fa un accesso separato per amministratori e clienti
        gli amministratori hanno una visualizzazione del dizionario delle vendite
        e lo stato corrente del dizionario inventario
        e vedere i guadagni totali
        '''

