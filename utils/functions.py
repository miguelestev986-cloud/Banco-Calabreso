from datetime import datetime as dt, timedelta as tdelta, date

from .users import agencias
from .constants import LIMITE_SAQUES, LIMITE_POR_SAQUE

def validar_conta():
    while True:
        agencia = input('Digite sua agência: ')
        if (agencia in agencias):
            while True:
                conta = input('Digite sua conta: ')
                if (conta in agencias[agencia]):
                    return agencia, conta
                else:
                    print('\nConta inválida, tente novamente.')
        else:
            print('\nAgência inválida.\nNão possui agência? Consulte nossa agência mais próxima em: https://bancopiton.com.br/agencias\n')

def validar_senha(agencia, conta):
    while True: 
        senha = input('Digite sua senha: ')
        if (agencias[agencia][conta]["senha"] == senha):
            print(f'\nAcesso aceito, bem vindo novamente Sr(a).{agencias[agencia][conta]["nome"]}!')
            return True
        else:
            print('\nSenha incorreta, tente novamente.')

def atualizar_extrato(agencia, conta, operacao, valor):
    agencias[agencia][conta]["extrato"].append(f'Data: {dt.now().replace(microsecond=0)}\nOperação: {operacao}\nValor: {agencias[agencia][conta]["moeda"]} {valor}')

def mostrar_extrato(agencia, conta):
    print('\n' + ' EXTRATO '.center(50, '~'))
    print('-' * 50 + '\n')
    for item in agencias[agencia][conta]["extrato"]:
        print(item.center(50, ' '))
        print('-' * 50)
    print('n' + ' FIM EXTRATO '.center(50, '~'))
    print(f'\nSaldo atual da conta: {agencias[agencia][conta]["moeda"]}{agencias[agencia][conta]["saldo"]}')

def depositar(agencia, conta):
    try:
        print(f'\nSeu saldo atual é de {agencias[agencia][conta]["moeda"]} {agencias[agencia][conta]["saldo"]}')
        deposito = float(input('Digite o valor do depósito: R$'))
        if (deposito > 0):
            agencias[agencia][conta]["saldo"] += deposito
            atualizar_extrato(agencia, conta, 'Depósito', deposito)
            return '\nDepósito realizado com sucesso!'
        else:
            return 'Insira um valor positivo para depósito. Tente novamente.'
    except ValueError:
        return 'Por favor digite apenas números e pontos para valores com casas decimais.'

def sacar(agencia, conta, saques):
    if (saques == LIMITE_SAQUES):
        print(f'O número máximo de saques diários(3) foi atingido, por favor espere até {date.today() + tdelta(days=1)} ou realize outra operação.')
    else:
        try:
            print(f'\nSeu saldo atual é de {agencias[agencia][conta]["moeda"]} {agencias[agencia][conta]["saldo"]}')
            saque = float(input('Digite o valor do saque: R$'))
            if (saque > LIMITE_POR_SAQUE):
                return '\nSaque excede o limite por saque(R$500,00), por favor tente novamente.'
            elif saque > agencias[agencia][conta]["saldo"]:
                return '\nSaldo insuficiente, tente novamente.'
            else:
                saques += 1
                agencias[agencia][conta]["saldo"] -= saque
                atualizar_extrato(agencia, conta, 'Saque', saque)
                return '\nSaque realizado com sucesso!'

        except ValueError:
            return 'Por favor digite apenas números e pontos para valores com casas decimais.'