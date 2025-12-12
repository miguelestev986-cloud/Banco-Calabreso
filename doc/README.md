```
   ___                       ___  _ __
  / _ )___ ____  _______    / _ \(_) /____  ___
 / _  / _ `/ _ \/ __/ _ \  / ___/ / __/ _ \/ _ \
/____/\_,_/_//_/\__/\___/ /_/  /_/\__/\___/_//_/
```
# Objetivo do Projeto
Esse é um reporitório de um projeto de um banco que, até o momento, permite realizar saques, depósitos e extrato, mas há mais recursos a serem adicionados, 
como: Banco de dados, Interface, Segurança, etc.

# Tecnologias

 <img 
        align="center" 
        alt="Python" 
        title="Python"
        width="30px" 
        style="padding-center: 10px;" 
        src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />

# Documentação (INCOMPLETA)

Dentro da pasta principal (onde ficam as pastas doc, src, tests e utils) rode o comando abaixo para iniciar o projeto:

```python
python3 -m src.main
# src/main.py é o arquivo em que o corpo do projeto está
```
Será impresso uma mensagens de boas vindas e serão feitos alguns inputs.

Responda com "0001" para ambas as perguntas.

```python
~~~~~~~~~~~~ Bem vindo ao Banco Piton ~~~~~~~~~~~~
             Seu banco de confiança!           

Qual a sua agência? 0001
Qual a sua conta? 0001
```

"Se eu errar a agência?"
O programa retornará que a agência é inválida e que caso o usuário não possua agência consulte uma agência mais próxima a ele em https://bancopiton.com.br/agencias (é um site ficticio) e perguntará qual é a sua agência até que a entrada seja válida (esteja no dicionário de agências em utils/users.py).

"E se eu errar a conta?"
O programa retornará que a conta é inválida e, assim como com a agência, perguntará qual é a sua conta até que a conta seja válida (esteja no dicionário da agência informada)

Se a agência e a conta forem válidas, o programa perguntará sua senha.

```python
~~~~~~~~~~~~ Bem vindo ao Banco Piton ~~~~~~~~~~~~
             Seu banco de confiança!           

Qual a sua agência? 0001
Qual a sua conta? 0001
Qual a sua senha? 1234
```

"Se eu errar a senha?"
O programa informará que a senha está incorreta e pedirá a senha até que a entrada seja a senha da conta pertencente à a agência informada.
