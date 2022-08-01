cartao = "378282246310005"
soma = somai = 0
for c in range(len(cartao)):
    if (c % 2 == 0):
        temp = int(cartao[c]) * 2
        if (temp >= 10):
            tempo = str(temp)
            temp = int(tempo[0]) + int(tempo[1])
        soma += temp
    else:
        somai += int(cartao[c])
result = soma + somai
print(result)