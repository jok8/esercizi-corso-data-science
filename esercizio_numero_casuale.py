import random


#imposto la condizione del gioco
gioco=True

#definisco la funzione numero_casuale
def numero_casuale():
    return random.randint(1,100)

numero_a_caso = numero_casuale()

#finchè il gioco è 'vero', giochiamo
while gioco:
    richiesta=input("vuoi giocare?\n")
    if richiesta == "si":
        #finchè la richiesta è sì, allora indovina un numero
        while richiesta=="si":
            numero = int(input("indovina un numero da 1 a 100"))
            #se il numero è uguale, allora ha indovinato, altrimenti dice se troppo alto o basso
            if numero == numero_a_caso:
                print("bravo, hai indovinato")
                richiesta=input("vuoi giocare?\n")
                continue
            elif numero != numero_a_caso:
                if numero > numero_a_caso:
                    print("numero troppo alto, ritenta")
                    continue
                if numero < numero_a_caso:
                    print("numero troppo basso, ritenta")
    #se la richiesta è no, non gioca
    if richiesta == "no":
        print("ok, non giochiamo allora")
        break
