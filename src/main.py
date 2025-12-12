from utils.functions import *
# Dentro de function há a importação do dicionário agencias, que contém os dados dos usuários, e da bibliotecas datetime

titulo = ' Bem vindo ao Banco Piton '
slogan = 'Seu banco de confiança!'
print(titulo.center(50, '~'))
print(slogan.center(50, ' ') + '\n')

menu = '''
=== Menu ===
D = Depositar
S = Sacar
E = Extrato
Q = Sair
'''
agencia, conta = validar_conta()
cliente = agencias[agencia][conta]
nsaques = 0
# Se eu deixasse a variável na função sacar, ela reiniciaria a cada chamada da função, então compartilhei entre main e functions

if (validar_senha(agencia,conta)):
    while True:
        print(menu)
        escolha = input('O que deseja fazer? ')

        if (escolha.upper() == 'D'):
            mensagem_d = depositar(agencia, conta)
            print(mensagem_d)
            
        elif (escolha.upper() == 'S'):
            mensagems, nsaques = sacar(agencia, conta, nsaques)
            print(mensagems)
        
        elif (escolha.upper() == 'E'):
            mostrar_extrato(agencia, conta)
        
        elif (escolha.upper() == 'Q'):
            print('\nObrigado por usar o Banco Piton. Volte sempre!')
            break

        else:
             print('\nPor favor digite uma opção válida.')