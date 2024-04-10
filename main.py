#Exercicio_16
#Faca um programa para uma loja de tintas. O programa devera pedir o tamanho em metros quadrados da area a ser pintada. 
#Considere que a cobertura da tinta e de 1 litro para cada 3 metros quadrados e que a tinta e vendida em latas de 18 litros, 
#que custam R$ 80,00. Informe ao usuario a quantidades de latas de tinta a serem compradas e o preco total.

import math

tamanho_area = float(input("Informe o tamanho da area a ser pintada em metros quadrados: "))

litros_necessarios = tamanho_area / 3
latas_necessarias = math.ceil(litros_necessarios / 18)
preco_total = latas_necessarias * 80

print(f"Voce precisara de {latas_necessarias} latas de tinta, totalizando R${preco_total: .2f}. ")


