import defs

from time import sleep
from time import ctime

def cadastroCliente():
    escolha = 0
    while escolha != 1:
        defs.clearTerminal()
        cliente = {
            'nome': str(input('Nome do cliente:\n')).lower(),
            'idade': int(input('Idade do cliente:\n')),
            'cpf': int(input('CPF do cliente:\n')),
            'senha': int(input('Senha do cliente:\n'))

        }

        for c in (cliente.items()):
            print(c)

        defs.sublinharPalavra('\nEstá tudo certo?\n[ 1 ] - Sim\n[ 2 ] - Não')
        escolha = int(input(''))

        if escolha == 1:
            defs.clearTerminal()
            defs.sublinharPalavra('Cliente sendo cadastrado...')
            sleep(2)
            defs.clearTerminal()
            defs.sublinharPalavra('Cliente cadastrado com sucesso')
            sleep(2)
            clientesCadastrados.append(cliente)
            break


carteira = 0
totalDeSaques = 0
totalDeDepositos = 0
depositosEfetuados = []
saquesEfetuados = []
clientesCadastrados = []


while True:

    # Menu
    defs.clearTerminal()
    defs.sublinharPalavra('The Bank')
    print('Opções: ')
    defs.sublinharPalavra(
        '[ 1 ] - Depósito\n[ 2 ] - Saque\n[ 3 ] - Extrato\n[ 4 ] - Cadastrar Cliente\n[ 5 ] - Clientes Cadastrados\n[ 6 ] - Acessar Conta\n[ 7 ] - Desligar')
    escolha = int(input(''))

    # Deposito
    if escolha == 1:
        defs.clearTerminal()
        defs.sublinharPalavra('Valor a ser depositado: ')
        valor = float(input(''))
        defs.clearTerminal()
        print('Deposito sendo efetuado...')
        sleep(2)
        defs.sublinharPalavra('Deposito efetuado com sucesso.')

        carteira = carteira + valor
        depositosEfetuados.append(valor)
        horaDeposito = ctime()
        totalDeDepositos = totalDeDepositos + 1

        print('Deseja fazer outra operação?')
        defs.sublinharPalavra('[ 1 ] - Sim\n[ 2 ] - Não')
        escolhaDep = int(input(''))
        if escolhaDep == 2:
            print(f'Você possui em sua conta:\nR${carteira}')
            print('Reiniciando...')
            sleep(2)

    # Saque
    elif escolha == 2:
        while True:
            defs.clearTerminal()
            defs.sublinharPalavra('Valor a ser sacado: ')
            valor = float(input(''))
            if carteira < valor:
                print(
                    f'Você possui apenas R${carteira}\nDeseja tentar novamente ?')
                defs.sublinharPalavra('[ 1 ] - Sim\n[ 2 ] - Não')
                tentativa = float(input(''))
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

    elif escolha == 3:
        defs.clearTerminal()
        print('Extrato sendo gerado...')
        sleep(2)
        defs.clearTerminal()

        defs.sublinharPalavra('Saques efetuados:')
        for c in (saquesEfetuados):
            print(c, horaSaque, '\n')

        if totalDeSaques == 1:
            print(f'Totalizando: {totalDeSaques} saque')
        elif totalDeSaques == 0:
            print('Nenhum saque foi efetuado')
        else:
            print(f'Totalizando: {totalDeSaques} saques')

        defs.sublinharPalavra('Depositos efetuados:')
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
        defs.sublinharPalavra(
            'Sua conta possui:\nR${:.2f} disponiveis'.format(carteira))

        input('\nPressione ENTER para voltar ao menu:\n')


    elif escolha == 4:
        cadastroCliente()


    elif escolha == 5:
        defs.clearTerminal()
        for c in (clientesCadastrados):
            print(c, '\n')
        input('Digite ENTER para voltar ao menu da aplicação')

    elif escolha == 6:
        defs.clearTerminal()
        print('Opção em desenvolvimento\n')
        input('Digite ENTER para voltar ao menu da aplicação')


    elif escolha == 7:
        print('O sistema está sendo encerrado...')
        sleep(2)
        defs.clearTerminal()
        print('Sistema encerrado.')
        sleep(1)
        defs.clearTerminal()
        break

    else:
        print("ERRO: Opção inválida\nDeseja tentar novamente?")
        defs.sublinharPalavra('[ 1 ] - Sim\n[ 2 ] - Não')
        continuar = int(input(''))
        if continuar == 2:
            break
