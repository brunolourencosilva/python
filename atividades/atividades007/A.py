# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:17/06/2024
# atividade007 A-Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou '0' para sair). 

import os


os.system('cls')

print('-'*70)
print('Programa que le um número indeterminado de notas\n(pressione "s" ou "0" para sair)')
print('='*70)

lista_notas = []

while True:
    notas = str(input('informe a nota: '))
    verificação = input('Continuar?(pressione "s" ou "0" para sair): '.lower())
    lista_notas.append(notas)
    if verificação == 's':
        continue
    else:
        break