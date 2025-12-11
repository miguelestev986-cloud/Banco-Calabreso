from utils.users import agencias
from utils.functions import validar_conta, validar_senha
from datetime import datetime as dt

print(' === Bem vindo ao Banco Piton ===\nSeu banco de confiança.')

LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500.00

saques = 0
menu = '''
=== Menu ===
D = Depositar
S = Sacar
E = Extrato
Q = Sair'''
agencia = input('Digite sua agência: ')
conta = input('Digite sua conta: ')
senha = input('Digite sua senha: ')

if (validar_conta(agencia, conta) == True):
    if (validar_senha(agencia, conta, senha) == True):
        print(menu)
        escolha = input('O que deseja fazer? ')

        if (escolha.upper() == 'D'):
            deposito = float(input('\nDigite o valor do depósito: '))
            agencias[agencia][conta]['saldo'] += deposito
            print(f'Depósito realizado com sucesso!\nSeu saldo atual é de {agencias[agencia][conta]["saldo"]}')
            agencias[agencia][conta]["extrato"].setdefault(dt.now(), f'Depósito: R$ {deposito:.2f}')
            
            escolha = input('\nDeseja continuar?(s/n) ')
            if escolha.upper() == 'N':
                print('Obrigado por usar o Banco Piton. Volte sempre!')
                break
                
        elif (escolha.upper() == 'S'):
            print(f'\nSeu saldo é de {agencias[agencia][conta]["saldo"]}.')

            while True:
                saque = float(input('\nDigite o valor do saque: '))
                if (saque > LIMITE_POR_SAQUE or saques >= LIMITE_SAQUES):
                          print('Saque excede o limite por saque ou o saldo atual da conta, tente novamente.')
                elif saque > agencias[agencia][conta]["saldo"]:
                            print('Saldo insuficiente, tente novamente.')
                else:
                    agencias[agencia][conta]["saldo"] -= saque
                    print(f'Saque realizado com sucesso!\n\nSeu saldo atual é de {agencias[agencia][conta]["saldo"]}.')
                    saques += 1
                    agencias[agencia][conta]["extrato"].setdefault(dt.now(), f'Saque: R$ {saque:.2f}')
                    break

                escolha = input('\nDeseja continuar?(s/n) ')
                if escolha.upper() == 'N':
                    print('Obrigado por usar o Banco Piton. Volte sempre!')
                    break
                
        elif (escolha.upper() == 'E'):
            print(f'\n=== EXTRATO ===')
            print(agencias[agencia][conta]["extrato"])
            print(f'Seu saldo atual é de: R$ {agencias[agencia][conta]["saldo"]:.2f}')
            print('='*15)

            escolha = input('\nDeseja continuar?(s/n) ')
            if escolha.upper() == 'N':
                print('Obrigado por usar o Banco Piton. Volte sempre!')
        else:
            print('\nObrigado por usar o Banco Piton. Volte sempre!')