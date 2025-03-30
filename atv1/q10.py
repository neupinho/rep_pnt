numero = int(input("Digite um número maior que 1: "))
eh_primo = True

for i in range(2, numero):
    if numero % i == 0:
        eh_primo = False
        break
if eh_primo:
    print("É primo mofio")
else:
    print("N é primo")
