import requests
print("Tell me a Pokemon character")
x=input()
x=x.lower()
link=f"https://pokeapi.co/api/v2/pokemon/{x}"
y=requests.get(link)
attribute=y.json()
print("\n")

print(f"{attribute['name']}\n")
for i  in attribute['abilities']:
    print(i['ability']['name'])
    print("\n")
for i  in attribute['forms']:
    print(i['name'])

for i  in attribute['game_indices']:
    print(i['game_index'])
    print(i['version']['name'])
print("\n")
print(f"{attribute['height']}\n")
print("\n")
for i  in attribute['held_items']:
    print(i['item'])
    for j in i['version_details']:
        print("\n",j)
print('\n')
print(f"{attribute['id']}\n")

for i  in attribute['moves']:
    print(i['move']['name'])
    for j in i['version_group_details']:
        print("\n",j)
        for k in j['version_group']:
            print("\n",k)
            


print(f"{attribute['order']}\n")
