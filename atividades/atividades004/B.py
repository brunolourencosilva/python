#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:23/04/2024
#atividade004 B-Faça um programa que receba o nome 'João da Silva' e, em seguida, substitua 'Silva' por 'Oliveira'.

import os


os.system('cls')

print('-'*70)
print('Programa que receba o nome "João da Silva" e, em seguida, substitua "Silva" por "Oliveira"')
print('='*70)

#Validação
nome = 'João da Silva'
substituicao = nome.replace("Silva", "Oliveira")

#saida
print(f'Nome original: {nome}')
print(f'Nome alterado: {substituicao}')