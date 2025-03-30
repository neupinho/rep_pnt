primos = []
numero = 2

while len(primos) < 100:
    eh_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break
    if eh_primo:
        primos.append(numero)
    numero += 1
print(primos)
