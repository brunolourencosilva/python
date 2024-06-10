# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:3/06/2024
# atividade005 J-Crie um programa que realiza a contagem de 1 até 100,
# usando apenas de números ímpares, ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo,
# assim como a soma dos mesmos.

import os


os.system('cls')

print('-'*70)
print('Programa que realiza a contagem de 1 até 100')
print('='*70)

contador = 0  # flag

while contador <= 100:
    contador += 1
    if (contador % 2 == 0): #pulando pares
        continue
    print(f'{contador}')
else:
    contador -= 1
    print('-'*70)
    print(f'\nQuantidade de numero impares: {contador}')
    
