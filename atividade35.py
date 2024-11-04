#Ler uma lista de 10 números reais e
#mostre-os na ordem inversa.


numeros = []

for i in range(10):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Exibe os números na ordem inversa
print("\nNúmeros na ordem inversa:")
for numero in reversed(numeros):
    print(numero)