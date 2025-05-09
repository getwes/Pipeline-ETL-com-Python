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
endpoint_products = "https://dummyjson.com/products/1"

endpoint_users = "https://dummyjson.com/users/"

for i in range(1,  10):
    data_users = extract_data(endpoint_users + str(i))
    load_data(data_users, "users")
