# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:12/07/2024
# atividade009 B-Crie uma função que cadastre o nome de uma aluno,a matrícula e a data de nascimento.
# Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for.

import os


os.system('cls')

dicionario = []

def dados(cadastro):
    dicionario.append(nome)
    dicionario.append(matricula)
    dicionario.append(data_nascimento)
    
    for i in dicionario:
        print(i)
    print('-'*70)
    
    return cadastro

print('Dados do aluno')
nome = input('Nome: ')
matricula = input('Matricula: ')
data_nascimento = input('Data de nascimento: ')
print('-'*70)

dados(cadastro=0)