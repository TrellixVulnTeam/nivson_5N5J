# Traitement des donnÃ©es de type CSV
# Nathan BIZON
# Le 14/03/2022

import csv
import os
# changement de dossier courrant

print(os.getcwd())

# import des donnÃ©es CSV

def import_data():
    out = []
    for i in range(4,11):
        path = f'data/Releve_Per0{i}.csv'
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

D = format_data(import_data())


def search_data(D,place,ctx,day):
    a=0
    b=0
    c=0
    d=0
    for x in D:
         if x["Lieu"]==place:
             if x["Conditions "]==ctx:
                 if x["Jour"]==day:
                     a=a+x["Valeur minimale"]
                     b=b+x["Valeur moyenne"]
                     c=c+x["Valeur maximale"]
                     d+=1
    a=a/d
    b=b/d
    c=c/d
    return a,b,c
