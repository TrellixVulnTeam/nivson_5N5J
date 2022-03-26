# Traitement des données de type CSV
# Nathan BIZON
# Le 14/03/2022

import csv
import os

def import_data(): # importe les données depuis les fichiers CSV | Crée par Nathan
    out = [] # on crée la liste qui contiendra toutes les valeurs
    for i in range(4,11): # pour chaque fichiers csv
        path = f'niveausonore/data/Releve_Per0{i}.csv' # path prend la valeur du chemin du fichier
        with open(path,'r',encoding='utf-8-sig') as f: # on ouvre le fichier
            out.append(list(csv.DictReader(f,delimiter=';'))) # on met les valeurs dans la liste
    return out # on retourne la liste de listes sous la forme [[{},{}],[{},{}]]

def format_data(D): # les valeurs sont de type str et on veut les convertir en int D = la liste de import_data(), on veut aussi empêcher les valeurs vides | Crée par Nathan
    out = [] # on crée la nouvelle liste
    for i in D: # pour chaque liste de liste
        for j in i: # pour chaque liste
            if j['Valeur minimale'] == '' or j['Valeur maximale'] == '' or j['Valeur moyenne'] == '': # s'il n'y a pas toutes les valeurs demandées
                pass # alors on ne l'insert pas dans la liste
            else:
                j['Valeur minimale'] = int(j['Valeur minimale']) # sinon on convertit les valeurs str en valeur int
                j['Valeur moyenne'] = int(j['Valeur moyenne'])
                j['Valeur maximale'] = int(j['Valeur maximale'])
                j['Id'] = int(j['Id'])
                out.append(j) # et on met chaque dictionnaire dans une liste
    return out # on retourne une liste de dictionnaire. La nouvelle liste est donc plus facile à traiter

def search_data(place,ctx,day): # fait un recherche des données et calcule leur moyennes | crée par Diego
    D = format_data(import_data()) # D prend la valeur de la liste de dictionnaires
    a=0 # initialisation des variables
    b=0
    c=0
    d=0
    for x in D: # pour chaque dictionnaires
         if x["Lieu"]==place: # si c'est la valeur recherché
             if x["Conditions "]==ctx:
                 if x["Jour"]==day:
                     a=a+x["Valeur minimale"] # on somme pour effectuer la moyenne
                     b=b+x["Valeur moyenne"]
                     c=c+x["Valeur maximale"]
                     d+=1 # d correspond au nombre de valeurs
    a=a/d # on effectue la moyenne
    b=b/d
    c=c/d
    return a,b,c # on renvoie un tuple conteanant la valeur minimale, la moyenne et la valeur maximale
