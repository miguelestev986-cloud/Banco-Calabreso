from .users import agencias

def validar_conta(agencia, conta):
    if (agencia in agencias):
        while True:
            if (conta in agencias[agencia]):
                return True
                break
            else:
                print("\nConta inválida, tente novamente.")
                conta = input('Digite sua conta: ')
    else:
        print("\nAgência inválida.\nNão possui agência? Consulte nossa agência mais próxima em: https://bancopiton.com.br/agencias")

def validar_senha(agencia, conta):
    while True: 
        senha = input('Digite sua senha: ')
        if (agencias[agencia][conta]['senha'] == senha):
                print(f"\nAcesso aceito, bem vindo novamente {agencias[agencia][conta]['nome']}")
                return True
                break
        else:
            print("\nSenha incorreta, tente novamente.")
