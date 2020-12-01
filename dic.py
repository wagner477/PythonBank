import os
import time
from defs import sublinharPalavra


def cadastroCliente():
    escolha = 0
    while escolha != 1:
        cliente = {
            'nome': input('Digite seu nome:\n'),
            'idade': int(input('Digite sua idade:\n')),
            'cpf': int(input('CPF:\n'))
        }

        print('Está tudo certo?\n[ 1 ] - Sim\n[ 2 ] - Não')
        escolha = int(input(''))
