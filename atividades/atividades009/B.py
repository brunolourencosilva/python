# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:1/07/2024
# atividade009 B-Utilizando o exercício anterior, adicione mais 2 elementos ao dicionário.

import os


os.system('cls')


print('='*70)
print('Programa que cria um dicionário com 4 elementos.')
print('-'*70)

# Declaração de dicionario
elementos = {}
periodica = []
# Declaração
contagem = -1

print('Tabela periodica')
print()

while True:
    contagem += 1
    continuar = str(input('Deseja Colocar um elemento? (s/n): ')).lower()

    if continuar == 's':
        print(f'Informe os dados do {contagem + 1}º elemento:')
        nome = str(input('Nome do elemento: '))
        simbolo = str(input('Simbolo do elemento: '))
        print('.'*70)

        elementos['nome'] = nome # Adiciona o nome do elemento ao dicionário
        elementos['simbolo'] = simbolo # Adiciona o símbolo do elemento ao dicionário
        periodica.append(elementos.copy()) # Adiciona uma cópia do dicionário 'elementos' à lista 'periodica'

    elif continuar == 'n':
        os.system('cls')
        print('-'*35)
        print('Parando programa!!')
        break
    else:
        print('Opção invalida!!')
        input('\nPressione Enter para continuar...')

print('-'*70)
print('Elementos adicionados: ')
for elementos in periodica: 
    for chave, valor in elementos.items():
        print(f'{chave}: {valor}') # Imprime cada chave e valor do dicionário 'elementos'
    print('-'*70)