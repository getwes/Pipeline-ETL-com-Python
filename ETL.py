import requests
#import pandas as pd
import json

#funcão para extrair dados da API DummyJSON
def extract_data(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"erro ao extrairi dados da API: {response.sttus_code}")



endpoint_users = "https://dummyjson.com/users/1"
endpoint_products = "https://dummyjson.com/products/1"

data_users = extract_data(endpoint_users)

print(data_users)
