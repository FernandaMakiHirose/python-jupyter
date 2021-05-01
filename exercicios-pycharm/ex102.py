# Dobrando os valores. 

def dobra(lts):
    pos = 0
    while pos < len(lts):
        lts[pos] *= 2
        pos += 1

valores = [2, 3, 4, 5, 6, 8]
dobra(valores)
print(valores)