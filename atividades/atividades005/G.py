#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:3/06/2024
#atividade005 G-Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.

import os


os.system('cls')

print('-'*70)
print('Programa que calcule os números primos em um \nintervalo pré-determinado pelo usuário')
print('='*70)

#entrada
inicio = int(input('Digite o valor inicial do intervalo: '))
fim = int(input('Digite o valor final do intervalo: '))
print('-'*70)

#validação
if inicio < 2:
    inicio = 2
    print('O valor colocado não é aceito como valor inicial')
    print('Ele sera trocado para 2,pois assim o programa funcionara corretamente')
    print('-'*70)

#processo

for numero_primo in range(inicio,fim):
    for divisor in range(2, int(numero_primo**0.5) + 1):#verificando se o numero é divisivel por 1 e por ele mesmo
        if numero_primo % divisor == 0: #verificando se o resto da divisão da 0,se for 0 é primo
            break
    else:
            print(f'{numero_primo}', end=' | ')

print()
print('-'*70)