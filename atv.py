# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.
# Inicializa a soma
soma = 0
valores  = float(input("digite um valor(0 para sair)"))
while valores != 0:
    soma += valores
    valores = float(input("digite um valor(0 para sair)"))
print(f"o resutado da soma é ={soma}")