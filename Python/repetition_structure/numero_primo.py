

# num = int(input("Digite um numero: "))
#
# for cont in range(num + 1):
#     if num % cont == 0:
#         print("Não é primo")
#         break
#     else:
#         print("É primo")
#         break


# numero = int(input("Digite um numero inteiro: "))
# primo = True
# for i in range(2, numero):
#     if numero % i == 0:
#         primo = False
#         print(f"{numero} não é primo! É divisível por {i}.")
# if primo:
#     print(f"{numero} é primo!")


# num = int(input("\nDigite um numero inteiro para saber se é primo: "))
# cont = 0
# div = []
#
# for i in range(num):
#     if num % (i + 1) == 0:
#         cont += 1
#         div.append(i + 1)
# if cont == 2:
#     print("O numero é primo divisivel por ", div)
# else:
#     print("O numero não é primo pois é divisivel por ", div)





# n = int(input("Digite um número inteiro: "))
# cont = 0
# i = 0
#
# while i <= n or cont < 2:
#     i = i + 1
#     x = n % i
#     if x == 0:
#         cont = cont + 1
#
#     if cont <= 2:
#         print("primo")
#         break
#     else:
#
#         print("não primo")
#         break