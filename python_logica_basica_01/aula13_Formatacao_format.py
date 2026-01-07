a = 'A'
b = 'B'
c = 1.11111111
d = 'parametro'
floaT = 'c={:.2f}'
formato_1 = floaT.format(c)
print(formato_1)

formato_2 = 'a={} b={} c{} d={nome4}'.format(a, b, c, nome4=d) # vem sempre na ordem dos argumentos dentro do format o 'nome4' é chamado de parametro pois referencia um argumento
print(formato_2)

formato_3 = 'a={0} a={0} a={2} b={1} c{2}'.format(a, b, c) # pegando pela ordem
print(formato_3)