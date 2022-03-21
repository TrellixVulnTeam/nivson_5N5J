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
        path = f'niveausonore/data/Releve_Per0{i}.csv'
        with open(path,'r',encoding='utf-8-sig') as f:
            out.append(list(csv.DictReader(f,delimiter=';')))
    return out

def format_data(D):
    out = []
    for i in D:
        for j in i:
            if j['Valeur minimale'] == '' or j['Valeur maximale'] == '' or j['Valeur moyenne'] == '':
                pass
            else:
                j['Valeur minimale'] = int(j['Valeur minimale'])
                j['Valeur moyenne'] = int(j['Valeur moyenne'])
                j['Valeur maximale'] = int(j['Valeur maximale'])
                j['Id'] = int(j['Id'])
                out.append(j)
    return out

data = format_data(import_data())

def search_data(D):
    pass
