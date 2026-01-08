"""
Operadores logicos
and(e) or(ou) not(não)

not - Usado para inverter expressões
not True = False
not False = True
"""

senha = input ('Senha: ')

if senha == '123456':
    print('Entrou')
else:
    print('Senha incorreta')

if senha != '123456':
    print('Senha incorreta')

if not senha: 
    print('Você não digitou nada.')
