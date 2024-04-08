#creo una classe punto
class Punto:
    x=0
    y=0
    #creo un metodo che dica di quanto vuoi spostarti
    def muovi(self):
        dx = int(input("di quanto vuoi spostarti sull'asse delle x?"))
        self.x += dx
        dy = int(input("di quanto vuoi spostarti sull'asse delle y?"))
        self.y += dy
        print("i nuovi valori sono", "x:",self.x,"","y:", self.y)
    
    #creo un metodo che dica di quanto ti sei sposato dall'origine
    def distanza_da_origine(self):
        print("La distanza da origine è: ", "x:",self.x, "", "y:", self.y)

#definisco l'oggetto z come Punto
z = Punto()

#stampo i punti di partenza di z
print(z.x,z.y)

#definisco x e y
z.x = 5
z.y = 7

#stampo la nuova distanza dall'origine
print(z.distanza_da_origine())