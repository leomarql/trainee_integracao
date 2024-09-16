#   Com as tuplas dos 20 primeiros colocados da Liga Juvenil de Futebol Amador,
#   ordenados de acordo com sua colocação, escreva na tela:
#       a) Os 5 primeiros times.
#       b) Os últimos 4 colocados.
#       c) Times em ordem alfabética.
#       d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético', 'Internacional',
         'Atlético-PR', 'Botafogo', 'Goias', 'Corinthians', 'Grêmio',
         'Bahia', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Vasco da Gama',
         'Cruzeiro', 'Fluminense', 'Chapecoence', 'CSA', 'Avaí')

print('5 primeiros colocados: ')
for i in range(20):
    if i < 5:
        print(times[i])

print('\n4 últimos colocados: ')
t = len(times)
for i in range(t-5, t):
    if i >= 16:
        print(times[i])

time = 'Chapecoence'
for i in range(20):
    if times[i] == time:
        print('\nposição da',time, ':',i+1, '\n') 

ordem = sorted(times)
for i in range(20):
    print(ordem[i])
