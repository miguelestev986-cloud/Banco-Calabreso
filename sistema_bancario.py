print(' === Bem vindo ao Banco Calabreso ===\n ')

def validar_usuario():
    global agencia 
    agencia = input('Digite sua agência: ')
    if (agencia in agencias):
        global conta
        conta = input('Digite sua conta: ')
        while True:
            if (conta in agencias[agencia]):
                return True
                break
            else:
                print("\nConta inválida, tente novamente.")
                conta = input('Digite sua conta: ')
    else:
        print("\nAgência inválida.\nNão possui agência? Consulte nossa agência mais próxima em: https://bancocalabreso.com.br/agencias")

def validar_senha():
    while True:
        global senha
        senha = input('Digite sua senha: ')
        if (agencias[agencia][conta]['senha'] == senha):
                print(f"\nAcesso aceito, bem vindo novamente {agencias[agencia][conta]['nome']}")
                return True
                break
        else:
            print("\nSenha incorreta, tente novamente.")

agencias = {
    "0001": {
        "0001" :{ 
            "nome" : 'Sr. Calabreso',
            "senha" : 'AQUI É BAHIA 1234',
            "saldo" : 1000.00,
            "extrato" : {
            }
        }
    }
}

LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500.00

menu = '''
=== Menu ===
D = Depositar
S = Sacar
E = Extrato
Q = Sair'''

saques = 0

if (validar_usuario() == True):
    if (validar_senha() == True):
        while True:
            print(menu)
            escolha = input('O que deseja fazer? ')

            if (escolha.upper() == 'D'):
                deposito = float(input('\nDigite o valor do depósito: '))
                agencias[agencia][conta]['saldo'] += deposito
                print(f'Depósito realizado com sucesso!\nSeu saldo atual é de {agencias[agencia][conta]["saldo"]}')
                agencias[agencia][conta]["extrato"] = f'Depósito: R$ {deposito:.2f}'

                escolha = input('\nDeseja continuar?(s/n) ')
                if escolha.upper() == 'N':
                    print('Obrigado por usar o Banco Calabreso. Volte sempre!')
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
                        agencias[agencia][conta]["extrato"] = f'Saque: -R$ {saque:.2f}'
                        break

                escolha = input('\nDeseja continuar?(s/n) ')
                if escolha.upper() == 'N':
                    print('Obrigado por usar o Banco Calabreso. Volte sempre!')
                    break
            
            elif (escolha.upper() == 'E'):
                print(f'=== EXTRATO ===')
                print({agencias[agencia][conta]["extrato"]})
                print(f'Seu saldo atual é de: R$ {agencias[agencia][conta]["saldo"]:.2f}')
                print('='*15)
            else:
                print('\nObrigado por usar o Banco Calabreso. Volte sempre!')
                break
