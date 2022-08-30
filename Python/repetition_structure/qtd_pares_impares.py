"""Ler 10 números e imprimir quantos são pares e quantos são ímpares."""

contador = 1
total_pares = 0
total_impares = 0

while contador <= 10:
    numero = int(input(f"Digite o {contador}° número: "))
    if numero % 2 == 0:
        total_pares += 1
    else:
        total_impares += 1
    contador += 1

print(f"O total de números pares é igual à {total_pares}")
print(f"O total de números ímpares é igual à {total_impares}")