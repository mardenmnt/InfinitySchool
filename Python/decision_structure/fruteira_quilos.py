"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

kg_morango = float(input('\nInforme quantos quilos de morango: ').replace(',', '.'))
kg_maca = float(input('Informe quantos quilos de maçã: ').replace(',', '.'))

# até 5 kg
morango_5_kg = 2.50
maca_5_kg = 1.80
total_morango = kg_morango * morango_5_kg
total_maca = kg_maca * maca_5_kg
total_compra = total_maca + total_morango

# acima de 5 kg
morango_acima = 2.20
maca_acima = 1.50
total_morango_acima = kg_morango * morango_acima
total_maca_acima = kg_maca * maca_acima
total_compra_acima = total_maca_acima + total_morango_acima

while kg_morango < 0 or kg_maca < 0:
    print('Valor inválido!')
    kg_morango = float(input('\nInforme quantos quilos de morango: ').replace(',', '.'))
    kg_maca = float(input('Informe quantos quilos de maçã: ').replace(',', '.'))

total_kg = kg_maca + kg_morango

if kg_morango <= 5 and kg_maca <= 5:
    print(f'\t{kg_morango:.2f} kg de morango ----- R$ {total_morango:.2f}\n'
          f'\t{kg_maca:.2f} kg de maçã ------- R$ {total_maca:.2f}\n'
          f'\tTotal a pagar --------- R$ {total_compra:.2f}')

elif 5 < kg_morango <= 8 or 5 < kg_maca <= 8:
    print(f'\t{kg_morango:.2f} kg de morango ----- R$ {total_morango_acima:.2f}\n'
          f'\t{kg_maca:.2f} kg de maçã -------- R$ {total_maca_acima:.2f}\n'
          f'\tTotal a pagar ---------- R$ {total_compra_acima:.2f}')

elif total_kg > 8 or total_compra_acima > 25:
    desconto = total_compra_acima * 0.10
    total_com_desconto = total_compra_acima - desconto
    print(f'\t{kg_morango:.2f} kg de morango --------- R$ {total_morango_acima:.2f}\n'
          f'\t{kg_maca:.2f} kg de maçã ------------- R$ {total_maca_acima:.2f}\n'
          f'\tTotal parcial --------------- R$ {total_compra_acima:.2f}\n'
          f'\tDesconto de 10% ------------- R$ {desconto:.2f}\n'
          f'\tTotal a pagar --------------- R$ {total_com_desconto:.2f}')