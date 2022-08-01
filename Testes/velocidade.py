lista = "ABCDEFGKLDJLSKLS"
tirar = "CEA"
lista = list(lista)
novalista = []
for c in enumerate(lista):
    if(c[1] in tirar):
        novalista.append(c[1])
print(novalista)