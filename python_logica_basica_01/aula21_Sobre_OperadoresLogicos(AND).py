"""
Docstring for python_logica_basica_01.aula21_Sobre_OperadoresLogicos

    Operadores Lógicos
and(e) or(ou) not(não)

and- Todas as condições precisam ser verdadeiras

Se qualquer valor for considerado falso, a expressao inteira será avaliadan aquele valor

Também existe o tipo None que é usado para representar um não valor
"""
entrada = input ('[E]ntrar [S]air')
senha_digitada = input('Senha: ')
senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
#Avaliação de curto circuito
print(True and False and True) #ele para no False e retorna False