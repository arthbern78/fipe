import json
import requests

veiculo = []

url = "http://fipeapi.appspot.com/api/1/carros/marcas.json"

# f = open("fipe.json", "w")
data = requests.get(url=url)
# f.close()

# for marca in data.json():
#  veiculo.append(marca)

# print(veiculo)

busca = input("Entre com o veiculo: ")
cont = 0

f = open("fipe.json", "w")
json.dump(data.json(), f, sort_keys=True, indent=4)
f.close()

g = open("filtro.json", "w")

for i in data.json():
    if i["name"] == busca:
        print("Veiculo: {}\nPreço: {}".format(i["name"], i["id"]))
        cont = cont + 1
        json.dump(i, g, sort_keys=True, indent=4)

g.close()

if cont == 0:
    print("Veiculo não localizado.")

