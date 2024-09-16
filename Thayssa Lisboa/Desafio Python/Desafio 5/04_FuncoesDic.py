"""
Para este exercicio, voce tem uma lista de dicionarios. Cada dicionario
tem as seguintes chaves:
 - lat: inteiro representando o valor de latitude
 - lon: inteiro representando o valor de longitude
 - name: nome do local
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Adicione um novo local a lista
waypoints.append({'lat': 42, 'lon': -124, 'name': 'a fourth place'})

# Modifique o dicionario com nome "a place" para uma longitude de valor -130 e mude seu nome para "not a real place"
t = len(waypoints)
for i in range(t):
    for j in waypoints[i]:
        if waypoints[i][j] == 'a place':
            waypoints[i]['lon'] = -130
            waypoints[i]['name'] = 'not a real place'
            break
         
# Crie um loop que escreva na tela todos os valores dos dicionarios da lista
for i in waypoints:
    print(i)