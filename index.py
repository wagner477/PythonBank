from defs import total
from defs import sublinharPalavra
from defs import cadastro
import os
from time import sleep
from time import ctime

# Função de cadastro


def cadastroCliente():
    escolha = 0
    while escolha != 1:
        os.system('cls')
        cliente = {
            'nome': str(input('Nome do cliente:\n')).lower(),
            'idade': int(input('Idade do cliente:\n')),
            'cpf': int(input('CPF do cliente:\n')),
            'senha': int(input('Senha do cliente:\n'))

        }

        for c in (cliente.items()):
            print(c)

        sublinharPalavra('\nEstá tudo certo?\n[ 1 ] - Sim\n[ 2 ] - Não')
        escolha = int(input(''))

        if escolha == 1:
            os.system('cls')
            sublinharPalavra('Cliente sendo cadastrado...')
            sleep(2)
            os.system('cls')
            sublinharPalavra('Cliente cadastrado com sucesso')
            sleep(2)
            clientesCadastrados.append(cliente)
            break


# Variaveis
carteira = 0
totalDeSaques = 0
totalDeDepositos = 0

depositosEfetuados = []
saquesEfetuados = []
clientesCadastrados = []


while True:

    # Menu
    os.system('cls')
    sublinharPalavra('The Bank')
    print('Opções: ')
    sublinharPalavra(
        '[ 1 ] - Depósito\n[ 2 ] - Saque\n[ 3 ] - Extrato\n[ 4 ] - Cadastrar Cliente\n[ 5 ] - Clientes Cadastrados\n[ 6 ] - Acessar Conta\n[ 7 ] - Desligar')
    escolha = int(input(''))

    # Deposito
    if escolha == 1:
        os.system('cls')
        sublinharPalavra('Valor a ser depositado: ')
        valor = int(input(''))
        os.system('cls')
        print('Deposito sendo efetuado...')
        sleep(2)
        sublinharPalavra('Deposito efetuado com sucesso.')

        carteira = carteira + valor
        depositosEfetuados.append(valor)
        horaDeposito = ctime()
        totalDeDepositos = totalDeDepositos + 1

        print('Deseja fazer outra operação?')
        sublinharPalavra('[ 1 ] - Sim\n[ 2 ] - Não')
        escolhaDep = int(input(''))
        if escolhaDep == 2:
            print(f'Você possui em sua conta:\nR${carteira}')
            print('Reiniciando...')
            sleep(2)

    # Saque
    elif escolha == 2:
        while True:
            os.system('cls')
            sublinharPalavra('Valor a ser sacado: ')
            valor = int(input(''))
            if carteira < valor:
                print(
                    f'Você possui apenas R${carteira}\nDeseja tentar novamente ?')
                sublinharPalavra('[ 1 ] - Sim\n[ 2 ] - Não')
                tentativa = int(input(''))
                if tentativa == 2:
                    print('Reiniciando...')
                    sleep(2)
                    break
            else:
                totalDeSaques = totalDeSaques + 1
                carteira = carteira - valor
                horaSaque = ctime()
                saquesEfetuados.append(valor)
                print('Saindo dinheiro...')
                sleep(2)
                print('Dinheiro sacado.')
                print(f'Seu saldo atual é de R${carteira}.')
                print('Reiniciando...')
                sleep(2)
                break

    # Extrato
    elif escolha == 3:
        os.system('cls')
        print('Extrato sendo gerado...')
        sleep(2)
        os.system('cls')

        sublinharPalavra('Saques efetuados:')
        for c in (saquesEfetuados):
            print(c, horaSaque, '\n')

        if totalDeSaques == 1:
            print(f'Totalizando: {totalDeSaques} saque')
        elif totalDeSaques == 0:
            print('Nenhum saque foi efetuado')
        else:
            print(f'Totalizando: {totalDeSaques} saques')

        sublinharPalavra('Depositos efetuados:')
        for x in (depositosEfetuados):
            print(x, horaDeposito, '\n')
        if totalDeDepositos == 1:
            print(f'Totalizando: {totalDeDepositos} deposito')
        elif totalDeDepositos == 0:
            print('Nenhum deposito foi efetuado')
        else:
            print(f'Totalizando: {totalDeDepositos} depositos')

        print('\nFoi cobrada uma taxa de R$0.50 por termos gerado o extrato')
        carteira = carteira - 0.50
        sublinharPalavra(
            'Sua conta possui:\nR${:.2f} disponiveis'.format(carteira))

        input('\nPressione ENTER para voltar ao menu:\n')

    # Cadastro

    elif escolha == 4:
        cadastroCliente()

    # Mostrar clientes cadastrados

    elif escolha == 5:
        os.system('cls')
        for c in (clientesCadastrados):
            print(c, '\n')
        input('Digite ENTER para voltar ao menu da aplicação')

    elif escolha == 6:
        os.system('cls')
        print('Opção em desenvolvimento\n')
        input('Digite ENTER para voltar ao menu da aplicação')

    # Desligar Sistema (Será tudo perdido)

    elif escolha == 7:
        print('O sistema está sendo encerrado...')
        sleep(2)
        os.system('cls')
        print('Sistema encerrado.')
        sleep(1)
        os.system('cls')
        break

    else:
        print("ERRO: Opção inválida\nDeseja tentar novamente?")
        sublinharPalavra('[ 1 ] - Sim\n[ 2 ] - Não')
        continuar = int(input(''))
        if continuar == 2:
            break
