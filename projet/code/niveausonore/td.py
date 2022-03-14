# Traitement des données de type CSV
# Nathan BIZON
# Le 14/03/2022

import csv
import os
# changement de dossier courrant

print(os.getcwd())

# import des données CSV

def import_data():
    out = []
    for i in range(4,11):
        path = f'data/Releve_Per0{i}.csv'
        with open(path,'r',encoding='utf-8-sig') as f:
            out.append(list(csv.DictReader(f,delimiter=';')))
    return out

print(import_data())