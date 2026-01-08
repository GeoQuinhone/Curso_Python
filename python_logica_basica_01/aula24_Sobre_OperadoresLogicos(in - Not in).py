"""
Operadores in(entre) e not in(nao esta entre)
String são interáveis(navegar item por item)
0 1 2 3 4 5 6
G e o v a n e
-6 -5 -4 -3 -2 -1 
"""

nome = 'Geovane'

print(nome[3]) #retorna a letra no indice 3 (v)
print(nome[-4])

print('o' in nome) # se a letra o esta entre as letras do nome retorna true
print('ova' in nome) 
print('ova' not in nome) 
print('z' in nome )

nome_2 = input('Digite o seu nome: ')
encontrar = input('O que deseja encontrar: ')

if encontrar in nome_2:
    print(f'{encontrar} está em {nome_2}')
else:
    print(f'{encontrar} não esta em {nome_2}')

