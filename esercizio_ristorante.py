tavoli = False
tavoli_occupati = 0
base = ["pan di spagna", "pan di zenzero", "pan au ciocolat"]
listino_base = [2,5,7]
farcitura = ["cioccolato", "marmellata di amarene", "marmellata di fragole"]
listino_farcitura = [10, 12, 15]
topping = ["cioccolato", "marmellata", "sciroppo d'acero"]
listino_topping = [5, 7, 10]
guadagni_base = [0,0,0]
guadagni_farcitura = [0,0,0]
guadagni_topping = [0,0,0]
guadagno_torta_tavolo = [0,0,0]
guadagno_totale = [0,0,0]


while tavoli == False:
    apertura = input("ristorante chiuso, scrivi apri per aprire\n")
    if apertura == "apri":
        tavoli = [1,2,3]

while tavoli == [1,2,3]:
    for i in tavoli:
        nome= input("benvenuti, mi dia un nome")
        print(f"perfetto, il vostro tavolo è il {i}")
        tavoli_occupati +=1
        scelta_base= int(input("scegliete un ingrediente per la base: 1 per pan di spagna, 2 per pan di zenzero, 3 per pan au ciocolat"))
        if scelta_base == 1:
            guadagni_base[0]= listino_base[0]
        elif scelta_base == 2:
            guadagni_base[1]= listino_base[1]
        elif scelta_base == 3:
            guadagni_base[2]= listino_base[2]
        scelta_farcitura = int(input("scegliete la farcitura: 1 per cioccolato, 2 per marmellata di amarene, 3 per marmellata di fragole"))
        if scelta_farcitura ==1:
            guadagni_farcitura[0] = listino_farcitura[0]
        elif scelta_farcitura ==2:
            guadagni_farcitura[1] = listino_farcitura[1]
        elif scelta_farcitura ==3:
            guadagni_farcitura[2] = listino_farcitura[2]
        scelta_topping = int(input("scegliete il topping: 1 per cioccolato, 2 per marmellata, 3 per sciroppo d'acero"))
        if scelta_topping ==1:
            guadagni_topping[0] = listino_topping[0]
        elif scelta_topping ==2:
            guadagni_topping[1] = listino_topping[1]
        elif scelta_topping ==3:
            guadagni_topping[2] = listino_topping[2]
        guadagno_torta_tavolo[i-1] = guadagni_base[scelta_base-1]+guadagni_farcitura[scelta_farcitura-1]+guadagni_topping[scelta_topping-1]
        print(f"Il prezzo della vostra torta è {guadagno_torta_tavolo[i-1]} euro")
        if tavoli_occupati == 3:
            break
    guadagno_totale= sum(guadagno_torta_tavolo)
    print(f"Il guadagno totale è {guadagno_totale} euro")
