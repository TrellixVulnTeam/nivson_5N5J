from django.shortcuts import render
from .td import search_data

# partie traitement des données


# partie requêtes

def index(request):
    a = ''
    if request.method == 'GET' and 'test' in request.GET:
        a = request.GET['test']
    return render(request, "index.html",context={"exemple":a})

def cour_prem_arbre(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('La cour des premières près des arbres', cdt,day)
        return render(request,'cour_prem_arbre.html',context=ctx)
    return render(request,'cour_prem_arbre.html')

def cour_prem_casier(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('La cour des premières près des casiers', cdt,day)
        return render(request,'cour_prem_casier.html',context=ctx)
    return render(request,'cour_prem_casier.html')

def espace_fumeur(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('L\'espace "fumeurs"', cdt,day)
        return render(request,'espace_fumeur.html',context=ctx)
    return render(request,'espace_fumeur.html')

def toilettes_prem(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Les toilettes des premières', cdt,day)
        
        return render(request,'toilettes_prem.html',context=ctx)
    return render(request,'toilettes_prem.html')

def salle_cours(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Une salle de cours', cdt,day)
        return render(request,'salle_cours.html',context=ctx)
    return render(request,'salle_cours.html')

def chapelle(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('La salle de devoirs "La chapelle"', cdt,day)
        return render(request,'chapelle.html',context=ctx)
    return render(request,'chapelle.html')

def salle_devoir_t(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('La salle de devoirs "T301"', cdt,day)
        return render(request,'salle_devoir_t.html',context=ctx)
    return render(request,'salle_devoir_t.html')

def salle_devoir_p(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('La salle de devoirs "P302"', cdt,day)
        return render(request,'salle_devoir_p.html',context=ctx)
    return render(request,'salle_devoir_p.html')

def couloir_prem(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Un couloir du batiment 1ères', cdt,day)
        return render(request,'couloir_prem.html',context=ctx)
    return render(request,'couloir_prem.html')

def couloir_sd(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Un couloir du batiment 2ndes', cdt,day)
        return render(request,'couloir_sd.html',context=ctx)
    return render(request,'couloir_sd.html')

def couloir_ter(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Un couloir du batiment terminales', cdt,day)
        return render(request,'couloir_ter.html',context=ctx)
    return render(request,'couloir_ter.html')

def foyer(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Le foyer', cdt,day)
        return render(request,'foyer.html',context=ctx)
    return render(request,'foyer.html')

def cdi(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Le CDI', cdt,day)
        return render(request,'cdi.html',context=ctx)
    return render(request,'cdi.html')

def rest_cdi(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Dans la file d\'attente pour la restauration près du CDI', cdt,day)
        return render(request,'rest_cdi.html',context=ctx)
    return render(request,'rest_cdi.html')

def rest_aquarium(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Dans la file d\'attente pour la restauration "Aquarium"', cdt,day)
        return render(request,'index.html',context=ctx)
    return render(request,'index.html')

def refectoire(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Le réfectoire des élèves', cdt,day)
        return render(request,'refectoire.html',context=ctx)
    return render(request,'refectoire.html')

def sport(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Le complexe sportif', cdt,day)
        return render(request,'sport.html',context=ctx)
    return render(request,'sport.html')

def cour_sd(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('La cour des secondes ', cdt,day)
        return render(request,'cour_sd.html',context=ctx)
    return render(request,'cour_sd.html')

def preau_ter(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Sous le préau de la cour des terminales', cdt,day)
        return render(request,'preau_ter.html',context=ctx)
    return render(request,'preau_ter.html')

def ref_prof(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('Le réfectoire des professeurs batiment P', cdt,day)
        return render(request,'ref_prof.html',context=ctx)
    return render(request,'ref_prof.html')

def sdp_pc(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('La salle des profs (coins ordinateurs ) batiment L', cdt,day)
        return render(request,'sdp_pc.html',context=ctx)
    return render(request,'sdp_pc.html')

def sdp_distrib(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('La salle des profs (coin distributeur) batiment L', cdt,day)
        return render(request,'sdp_distrib.html',context=ctx)
    return render(request,'sdp_distrib.html')
    
def sdp_ref(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        ctx = search_data('La salle des profs (réfectoire) batiment L', cdt,day)
        return render(request,'sdp_ref.html',context=ctx)
    return render(request,'sdp_ref.html')
