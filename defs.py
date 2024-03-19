import os
from time import sleep


def total():
    os.system('cls' if os.name == 'nt' else 'clear')
    x = int(input("Qual numero gostaria de começar a contagem? \n"))
    y = int(input("Qual numero gostaria de terminar a contagem? \n"))
    while x < y:
        x = x + 1
        print(x)


def sublinharPalavra(palavra):
    linha = str(palavra).__len__()
    underline = ('-' * linha)
    print(f'{underline}\n{palavra}\n{underline}')

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def cadastro(nome, idade, cpf, cidade):
    escolha = 0

    while escolha != 2:

        nome = input('Digite seu nome:\n')
        os.system('cls' if os.name == 'nt' else 'clear')

        idade = input('Digite sua idade:\n')
        os.system('cls' if os.name == 'nt' else 'clear')

        cpf = int(input('Digite seu CPF:\n'))
        os.system('cls' if os.name == 'nt' else 'clear')

        cidade = input('Digite sua cidade:\n')
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'nome: {nome}\nidade: {idade}\nCPF: {cpf}\nCidade: {cidade}\n')

        print('Está tudo certo?\n[ 1 ] - Sim\n[ 2 ] - Não')
        escolha = int(input(''))
