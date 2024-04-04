#faccio inserire un numero
numero = int(input("Inserisci un numero\n"))

#stampo i numeri dal numero scelto fino a 0, con step 1
for i in range(numero, -1, -1):
    print(i)

#chiedo se vuole ripetere il gioco
ripetizione = int(input("Vuoi ripetere? Se sì, scrivi 1. Se no, scrivi 0"))

#finchè vuole ripetere il gioco, gli chiedo un numero e gli restituisco il countdown
while ripetizione == 1:
    if ripetizione==1:
        numero = int(input("Inserisci un numero\n"))
        for i in range(numero, -1, -1):
            print(i)
        ripetizione = int(input("Vuoi ripetere? Se sì, scrivi 1. Se no, scrivi 0\n"))
    else:
        break