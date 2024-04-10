# Exercicio 2

import math 

tamanho_area = float(input("Informe o tamanho da area a ser pintada em metros quadrados: "))

litros_necessarios = tamanho_area / 6

# Comprar apenas latas de 18 litros
latas_necessarias = math.ceil(litros_necessarios / 18)
preco_total_latas = latas_necessarias * 80

# Comprar apenas galoes de 3,6 litros
galoes_necessarios = math.ceil(litros_necessarios / 3.6)
preco_total_galoes = galoes_necessarios * 25

# Misturar latas e galoes
latas_para_comprar = math.floor(litros_necessarios / 18)
litros_restantes = litros_necessarios - (latas_para_comprar * 18)
galoes_para_comprar = math.ceil(litros_restantes / 3.6)
preco_total_mix = (latas_para_comprar * 80) + (galoes_para_comprar * 25)

print(f"Comprando apenas latas de 18 litros, voce precisara de {latas_necessarias} latas, totalizando R$ {preco_total_latas:.2f}.")
print(f"Comprando apenas galoes de 3,6 litros, voce precisara de {galoes_necessarios} galoes, totalizando R$ {preco_total_galoes:.2f}.")
print(f"Misturando latas e galoes, voce precisara de {latas_para_comprar} latas e {galoes_para_comprar} galoes, totalizando R$ {preco_total_mix:.2f}.")
