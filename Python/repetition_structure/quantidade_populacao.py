"""
População A tem 80000 pessoas
População B tem 200000 pessoas
Taxa crescimento população A = 3% anual e a população B = 1,5%
Quanto tempo levará para a população A ultrapassar ou ficar igual à população B?
"""

populacao_a = 80000
populacao_b = 200000
taxa_a = 0.03
taxa_b = 0.015
contador = 0

print(f"No ano Atual:")
print(f"A população de A é de {populacao_a}.")
print(f"A população de B é de {populacao_b}.")

while True:
    populacao_a = populacao_a + (populacao_a * taxa_a)
    populacao_b = populacao_b + (populacao_b * taxa_b)
    contador += 1
    print(f"No ano {contador}:")
    print(f"A população de A será: {populacao_a}.")
    print(f"A população de B será: {populacao_b}.")
    if populacao_a >= populacao_b:
        break

print(f"\nDepois de {contador} anos, a população de A passará a populaçao de B.")
