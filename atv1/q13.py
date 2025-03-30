salario = float(input("Digite o salário inicial: "))
anos = int(input("Digite a quantidade de anos: "))
percentual = 0.01

for i in range(anos):
    salario += salario * percentual
    percentual *= 2
print("Salário final: R$", salario)
