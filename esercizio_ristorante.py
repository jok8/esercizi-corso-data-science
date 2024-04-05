tavoli = False
clienti = [1,2,3]
base = ["pan di spagna", "pan di zenzero", "pan au ciocolat"]
listino_base = [2,5,7]
farcitura = ["cioccolato", "marmellata di amarene", "marmellata di fragole"]
listino_farcitura = [10, 12, 15]
topping = ["cioccolato", "marmellata", "sciroppo d'acero"]
listino_topping = [5, 7, 10]
guadagni_base = False
guadagni_farcitura = False
guadagni_topping = False
guadagno_torta_tavolo = [0,0,0]
guadagno_totale = False


while tavoli == False:
    apertura = input("ristorante chiuso, scrivi apri per aprire\n")
    if apertura == "apri":
        tavoli = True

while tavoli == True:
    nome= input("benvenuti, mi dia un nome")
    for i in clienti:
        if i==0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print(f"perfetto, il vostro tavolo è il {i}")
            clienti[i]==nome
        scelta_base= input("scegliete un ingrediente per la base")
        if scelta_base == 1:
            guadagni_base[scelta_base-1]= listino_base[scelta_base-1]
        elif scelta_base == 2:
            guadagni_base[scelta_base-1]= listino_base[scelta_base-1]
        elif scelta_base == 3:
            guadagni_base[scelta_base-1]= listino_base[scelta_base-1]
        scelta_farcitura = input("scegliete la farcitura")
        if scelta_farcitura ==1:
            guadagni_farcitura[scelta_farcitura-1] = listino_farcitura[scelta_farcitura-1]
        elif scelta_farcitura ==2:
            guadagni_farcitura[scelta_farcitura-1] = listino_farcitura[scelta_farcitura-1]
        elif scelta_farcitura ==3:
            guadagni_farcitura[scelta_farcitura-1] = listino_farcitura[scelta_farcitura-1]
        scelta_topping = input("scegliete il topping")
        if scelta_topping ==1:
            guadagni_topping[scelta_topping-1] = listino_topping[scelta_topping-1]
        elif scelta_topping ==2:
            guadagni_topping[scelta_topping-1] = listino_topping[scelta_topping-1]
        elif scelta_topping ==3:
            guadagni_topping[scelta_topping-1] = listino_topping[scelta_topping-1]
        for i in guadagno_torta_tavolo:
            guadagno_torta_tavolo[i] = guadagni_base[i]+guadagni_farcitura[i]+guadagni_topping[i]
            print(f"Il prezzo della vostra torta è {guadagno_torta_tavolo[i]} euro")
    guadagno_totale= sum(guadagno_torta_tavolo)
    print(f"Il guadagno totale è {guadagno_totale} euro")