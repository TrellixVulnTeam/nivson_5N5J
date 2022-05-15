# views.py
# gestion des requêtes HTTP
# seule la première fonction sera expliqué car toutes ont la même structure

from django.shortcuts import render
from .td import *

# partie requêtes

def index(request):
    return render(request, "index.html")

def cour_prem_arbre(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']): # la requête est de type GET et a des éléments ?
        cdt = request.GET['condition'] # prendre le contenu de la variable condition
        day = request.GET['jour'] # prendre le conenu de la variable jour
        ctx = search_data("La cour des premières près des arbres",cdt,day) # on cherche les données dans les fichiers csv
        return render(request,'cour_prem_arbre.html',context=ctx) # on retourne la page avec le dictionnaire. Dans les pages HTML elles sont indiqué entre deux acolades
    return render(request,'cour_prem_arbre.html',context = search_data("La cour des premières près des arbres","Lundi","Récréation du matin")) # s'il n'y a pas d'éléments alors on affiche juste la page

def cour_prem_casier(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("La cour des premières près des casiers",cdt,day)
        return render(request,'cour_prem_casier.html',context=ctx)
    return render(request,'cour_prem_casier.html',context = search_data("La cour des premières près des casiers","Lundi","Récréation du matin"))

def espace_fumeur(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("L'espace \"fumeurs\"",cdt,day)
        return render(request,'espace_fumeur.html',context=ctx)
    return render(request,'espace_fumeur.html',context = search_data("L'espace \"fumeurs\"","Lundi","Récréation du matin"))

def toilettes_prem(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Les toilettes des premières",cdt,day)
        return render(request,'toilettes_prem.html',context=ctx)
    return render(request,'toilettes_prem.html',context = search_data("Les toilettes des premières","Lundi","Récréation du matin"))

def salle_cours(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Une salle de cours",cdt,day)
        return render(request,'salle_cours.html',context=ctx)
    return render(request,'salle_cours.html',context = search_data("Une salle de cours","Lundi","Récréation du matin"))

def chapelle(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("La salle de devoirs \"La chapelle\"",cdt,day)
        return render(request,'chapelle.html',context=ctx)
    return render(request,'chapelle.html',context = search_data("La salle de devoirs \"La chapelle\"","Lundi","Récréation du matin"))

def salle_devoir_t(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("La salle de devoirs \"T301\"",cdt,day)
        return render(request,'salle_devoir_t.html',context=ctx)
    return render(request,'salle_devoir_t.html',context = search_data("La salle de devoirs \"T301\"","Lundi","Récréation du matin"))

def salle_devoir_p(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("La salle de devoirs \"P302\"",cdt,day)
        return render(request,'salle_devoir_p.html',context=ctx)
    return render(request,'salle_devoir_p.html',context = search_data("La salle de devoirs \"P302\"","Lundi","Récréation du matin"))

def couloir_prem(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Un couloir du batiment 1ères",cdt,day)
        return render(request,'couloir_prem.html',context=ctx)
    return render(request,'couloir_prem.html',context = search_data("Un couloir du batiment 1ères","Lundi","Récréation du matin"))

def couloir_sd(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Un couloir du batiment 2ndes",cdt,day)
        return render(request,'couloir_sd.html',context=ctx)
    return render(request,'couloir_sd.html',context = search_data("Un couloir du batiment 2ndes","Lundi","Récréation du matin"))

def couloir_ter(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Un couloir du batiment terminales",cdt,day)
        return render(request,'couloir_ter.html',context=ctx)
    return render(request,'couloir_ter.html',context = search_data("Un couloir du batiment terminales","Lundi","Récréation du matin"))

def foyer(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Le foyer",cdt,day)
        return render(request,'foyer.html',context=ctx)
    return render(request,'foyer.html',context = search_data("Le foyer","Lundi","Récréation du matin"))

def cdi(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Le CDI",cdt,day)
        return render(request,'cdi.html',context=ctx)
    return render(request,'cdi.html',context = search_data("Le CDI","Lundi","Récréation du matin"))

def rest_cdi(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Dans la file d'attente pour la restauration près du CDI",cdt,day)
        return render(request,'rest_cdi.html',context=ctx)
    return render(request,'rest_cdi.html',context = search_data("Dans la file d'attente pour la restauration près du CDI","Lundi","Récréation du matin"))

def rest_aquarium(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Dans la file d'attente pour la restauration \"Aquarium\"",cdt,day)
        return render(request,'rest_aquarium.html',context=ctx)
    return render(request,'rest_aquarium.html',context = search_data("Dans la file d'attente pour la restauration \"Aquarium\"","Lundi","Récréation du matin"))

def refectoire(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Le réfectoire des élèves",cdt,day)
        return render(request,'refectoire.html',context=ctx)
    return render(request,'refectoire.html',context = search_data("Le réfectoire des élèves","Lundi","Récréation du matin"))

def sport(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Le complexe sportif",cdt,day)
        return render(request,'sport.html',context=ctx)
    return render(request,'sport.html',context = search_data("Le complexe sportif","Lundi","Récréation du matin"))

def cour_sd(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("La cour des secondes ",cdt,day)
        return render(request,'cour_sd.html',context=ctx)
    return render(request,'cour_sd.html',context = search_data("La cour des secondes ","Lundi","Récréation du matin"))

def preau_ter(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Sous le préau de la cour des terminales",cdt,day)
        return render(request,'preau_ter.html',context=ctx)
    return render(request,'preau_ter.html',context = search_data("Sous le préau de la cour des terminales","Lundi","Récréation du matin"))

def ref_prof(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("Le réfectoire des professeurs batiment P",cdt,day)
        return render(request,'ref_prof.html',context=ctx)
    return render(request,'ref_prof.html',context = search_data("Le réfectoire des professeurs batiment P","Lundi","Récréation du matin"))

def sdp_pc(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("La salle des profs (coins ordinateurs ) batiment L",cdt,day)
        return render(request,'sdp_pc.html',context=ctx)
    return render(request,'sdp_pc.html',context = search_data("La salle des profs (coins ordinateurs ) batiment L","Lundi","Récréation du matin"))

def sdp_distrib(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("La salle des profs (coin distributeur) batiment L",cdt,day)
        return render(request,'sdp_distrib.html',context=ctx)
    return render(request,'sdp_distrib.html',context = search_data("La salle des profs (coin distributeur) batiment L","Lundi","Récréation du matin"))

def sdp_ref(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data("La salle des profs (réfectoire) batiment L",cdt,day)
        return render(request,'sdp_ref.html',context=ctx)
    return render(request,'sdp_ref.html',context = search_data("La salle des profs (réfectoire) batiment L","Lundi","Récréation du matin"))
