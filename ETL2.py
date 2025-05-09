import requests
#import pandas as pd
import json

#ETL - extract, Trasform, Load

#funcão para extrair dados da API DummyJSON
def extract_data(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"erro ao extrairi dados da API: {response.sttus_code}")
        return None

def load_data(data,path):
    id = data["id"]
    #dentro da pasta path, criar um arquivo json com o nome do arquivo sendo o id o nome do arquivo .json
    with open(f"{path}/{id}.json", "w") as file:
        json.dump(data, file)


def loop_load_data(endpoint, path):
    
    i = 1
    while True:
        data = extract_data(endpoint + str(i))
        if data:
            load_data(data, path)
        else:
             print(f"erro ao etrair dados da api: {data}")
             break
    i += 1
loop_load_data("https://dummyjson.com/users/", "users")
loop_load_data("https://dummyjson.com/products/", "products")