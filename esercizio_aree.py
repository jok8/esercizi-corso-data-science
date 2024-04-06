
def area_triangolo(b,h):
    return (b*h)/2

def area_quadrato(l):
    return l**2

def area_rettangolo(b,h):
    return b*h

triangolo=0
quadrato=0
rettangolo=0
aree=[0,0,0]

print(triangolo)

while aree==[0,0,0] and triangolo==0 and quadrato==0 and rettangolo==0:
    tipo_area=input(("quale area vuoi calcolare? se vuoi far finire il gioco scrivi fine "))
    if tipo_area=="triangolo":
        b_t=int(input("dimmi il valore della base"))
        h_t=int(input("dimmi il valore dell'altezza"))
        triangolo=area_triangolo(b_t,h_t)
        aree[0]=triangolo
    elif tipo_area=="quadrato":
        l=int(input("dimmi valore del lato"))
        quadrato=area_quadrato(l)
        aree[1]=quadrato
    elif tipo_area=="rettangolo":
        b_r = int(input("dimmi il valore della base"))
        h_r = int(input("dimmi il valore dell'altezza"))
        rettangolo = area_rettangolo(b_r,h_r)
        aree[2]=rettangolo
    else:
            break
        
condizione_di_chiusura = input(f"le aree sono:\narea triangolo = {triangolo}\narea quadrato= {quadrato}\narea rettangolo = {rettangolo}\nScrivi esci per uscire e resettare le aree")
if condizione_di_chiusura == "esci":
    aree = [0,0,0]
    print(f"Le aree sono {aree}, arrivederci")
