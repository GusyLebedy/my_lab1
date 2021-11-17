import json

file = open('pokemon_full.json')
pokemon_full = file.read()
file.close()

print('Общее количество символов в файле:', len(pokemon_full))

meter = 0
for symbol in pokemon_full:
    if symbol.isalnum():
        meter += 1
print('Общее количесто символов без пробелов и знаков препинания: ', meter)

pokemon_list = json.loads(pokemon_full)
max_detail = 0
pokemon_name = ''
for char in pokemon_list:
    max_detail = max(len(char['description']), max_detail)
    if len(char['description']) == max_detail:
        pokemon_name = char['name']
print('Покемон', pokemon_name, 'имеет наиболее длинное описание')

amount = 0
for capabilities in pokemon_list:
    for capability in capabilities['abilities']:
        amount = max(len(capability.split()), amount)

for capabilities in pokemon_list:
    for capability in capabilities['abilities']:
        if amount == len(capability.split()):
            print('Названия умений, которые содержат больше всего слов:', capability)
