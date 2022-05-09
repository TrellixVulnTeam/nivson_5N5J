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

def search_data(place,ctx,day):
    '''
    Rôle :
        Déterminer des statistiques à partir de données

    Parameters
    ----------
    place : str
        Lieu des données
    ctx : str
        Condition des données
    day : str
        Jour des données

    Returns
    -------
    Dictionnaire
        Dictionnaire de statistiques
    Variable "moymin"
        La moyenne des valeurs minimales
    Variable "moymoy"
        La moyenne des valeurs moyennes
    Variable "moymax"
        La moyenne des valeurs maximales
    Variable "mintemp"
        La valeur minimale
    Variable "med"
        La médiane
    Variable "maxtemp"
        La valeur maximale
    Variable "p_fatiguant"
        La proportion de valeur entre 80 et 90dB
    Variable "p_dangereux"
        La proportion de valeur au dessus de 90dB

    '''
    D = format_data(import_data()) #table
    moymin,moymoy,moymax,eff,maxtemp=0,0,0,0,0 #Initialisation des variables
    mintemp=999 #Initialisation d'une variable pour avoir le minimum temporaire
    med,fati,dang=[],[],[] #Initialisation de listes
    for x in D: #recherche dans le data
         if x["Lieu"]==place: #correspondance avec le lieu
             if x["Conditions "]==ctx: #correspondance avec la condition
                 if x["Jour"]==day: #correspondance avec le jour
                     moymin,moymoy,moymax=moymin+x["Valeur minimale"],moymoy+x["Valeur moyenne"],moymax+x["Valeur maximale"] #accumulation des valeurs dans les moyennes
                     eff+=1 #compteur d'effectif
                     if mintemp>x["Valeur minimale"]:
                         mintemp=x["Valeur minimale"] #calcul de la valeur minimale
                     med.append(x["Valeur minimale"]),med.append(x["Valeur moyenne"]),med.append(x["Valeur maximale"]),med.sort() #Création d'un tableau de toutes les valeurs puis trié
                     if maxtemp<x["Valeur maximale"]:
                         maxtemp=x["Valeur maximale"] #calcul de la valeur maximale
                     fati.append([med[i] for i in range(len(med)) if med[i]>=80 and med[i]<=90]) #Création d'un tableau de valeurs au dessus de 80
                     dang.append([med[i] for i in range(len(med)) if med[i]>=90]) #Création d'un tableau de valeurs au dessus de 90
    out = {
        "moymin":round(moymin/eff,1),
        "moymoy":round(moymoy/eff,1),
        "moymax":round(moymax/eff,1),
        "mintemp":mintemp,
        "med":med[int((len(med)/2)-1)],
        "maxtemp":maxtemp,
        "p_fatiguant":round((len(fati[-1])*100)/(len(med)),1),
        "p_dangereux":round((len(dang[-1])*100)/(len(med)),1)
          }
    return out #Arrondi à 10^-1 de la moyenne des valeurs minimales,Arrondi à 10^-1 de la moyenne des valeurs moyennes,Arrondi à 10^-1 de la moyenne des valeurs maximales,Renvoi de la valeur minimale,Renvoi de la valeur médiane, Renvoi de la valeur maximale,Arrondi à 10^-1 de la proportion de valeurs au dessus de 80,Arrondi à 10^-1 de la proportion de valeurs au dessus de 90
