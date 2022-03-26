# views.py
# gestion des requêtes HTTP
# seule la première fonction sera expliqué car toutes ont la même structure

from django.shortcuts import render
from .td import *

# partie traitement des données


# partie requêtes

def index(request):
    return render(request, "index.html")

def cour_prem_arbre(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']): # la requête est de type GET et a des éléments ?
        cdt = request.GET['condition'] # prendre le contenu de la variable condition
        day = request.GET['jour'] # prendre le conenu de la variable jour
        mini,moy,maxi = search_data("La cour des premières près des arbres",cdt,day) # on cherche les données dans les fichiers csv
        ctx = {'mini':mini,'moy':moy,'maxi':maxi} # on met les données dans un dictionnaire
        return render(request,'index.html',context=ctx) # on retourne la page avec le dictionnaire. Dans les pages HTML elles sont indiqué entre deux acolades
    return render(request,'index.html') # s'il n'y a pas d'éléments alors on affiche juste la page

def cour_prem_casier(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La cour des premières près des casiers",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def espace_fumeur(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("L'espace \"fumeurs\"",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def toilettes_prem(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Les toilettes des premières",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def salle_cours(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Une salle de cours",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def chapelle(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La salle de devoirs \"La chapelle\"",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def salle_devoir_t(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La salle de devoirs \"T301\"",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def salle_devoir_p(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La salle de devoirs \"P302\"",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def couloir_prem(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Un couloir du batiment 1ères",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def couloir_sd(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Un couloir du batiment 2ndes",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def couloir_ter(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Un couloir du batiment terminales",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def foyer(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Le foyer",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def cdi(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Le CDI",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def rest_cdi(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Dans la file d'attente pour la restauration près du CDI",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def rest_aquarium(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Dans la file d'attente pour la restauration \"Aquarium\"",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def refectoire(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Le réfectoire des élèves",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def sport(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Le complexe sportif",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def cour_sd(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La cour des secondes ",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def preau_ter(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Sous le préau de la cour des terminales",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def ref_prof(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Le réfectoire des professeurs batiment P",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def sdp_pc(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La salle des profs (coins ordinateurs ) batiment L",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def sdp_distrib(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La salle des profs (coin distributeur) batiment L",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def sdp_ref(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La salle des profs (réfectoire) batiment L",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')
