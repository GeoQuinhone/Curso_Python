nome = 'Geovane Quinhone'
altura = 1.77
peso = 80
imc = peso / (altura * altura)


"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura' #usando variaveis dentro desse texto usando chaves o :.2f formatando as casas decimais após o .
print(linha_1)

linha_2 = f'pesa {peso} quilos e seu IMC é'
print(linha_2)

linha_3 = f'{imc:.2f}'
print(linha_3)

#print(nome, 'tem' , altura, 'de altura,',)
#print('pesa' , peso , 'quilos e seu IMC é',)
#print (imc)