"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

minimo_nome = 3
while True:
    nome = input('\nInforme seu nome: ')
    if len(nome) <= minimo_nome:
        print('O nome precisa ter no mínimo 4 letras\n'
              'Tente novamente')
        continue
    else:
        idade = int(input('\nQual sua idade? '))
        if idade < 0 or idade > 150:
            print('Idade invlida!\n'
                  'Tente novamente')
            continue
        else:
            salario = float(input('\nInforme seu salário: ').replace(',', '.'))
            if salario <= 0:
                print('Salário inválido\n'
                      'Tente novamente')
                continue
            else:
                sexo = input('\nF -> feminino / M - masculino\n'
                             'Qual seu sexo? ').upper()
                if sexo != 'F' and sexo != 'M':
                    print('Opção inválida!\n'
                          'Tente novamente')
                    continue
                else:
                    if sexo == 'F':
                        sexo = 'Feminino'
                    elif sexo == 'M':
                        sexo = 'Masculino'
                    estado_civil = input('\nS - solteiro(a)\n'
                                         'C - casado(a)\n'
                                         'V - viúvo(a)\n'
                                         'D - divorsiado(a)\n'
                                         'Qual seu estado civil? ').upper()
                    if estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
                        print('Opção inválida!\n'
                              'Tente novamente')
                        continue
                    else:
                        if estado_civil == 'S':
                            estado_civil = 'Solteiro(a)'
                        elif estado_civil == 'C':
                            estado_civil = 'Casado(a)'
                        elif estado_civil == 'V':
                            estado_civil = 'Viúvo(a)'
                        elif estado_civil == 'D':
                            estado_civil = 'Divorsiado(a)'
                        print('\nCadastro realizado com sucesso!')
                        print(f'Seu nome: {nome}')
                        print(f'Sua idade: {idade}')
                        print(f'Seu salário é: R$ {salario}')
                        print(f'Você é do sexo {sexo}')
                        print(f'Seu estado civil: {estado_civil}')
                        break
