from django.shortcuts import render
from .td import *

# partie traitement des données


# partie requêtes

def index(request):
    a = ''
    if request.method == 'GET' and 'test' in request.GET:
        a = request.GET['test']
    return render(request, "index.html",context={"exemple":a})

def cour_prem_arbre(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def cour_prem_casier(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def espace_fumeur(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def toilettes_prem(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def salle_cours(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def chapelle(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def salle_devoir_t(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def salle_devoir_p(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def couloir_prem(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def couloir_sd(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def couloir_ter(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def foyer(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def cdi(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def rest_cdi(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def rest_aquarium(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def refectoire(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def sport(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def cour_sd(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def preau_ter(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def ref_prof(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def sdp_pc(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')

def sdp_distrib(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')
    
def sdp_ref(request):
    if request.method == 'GET' and all(q in request.GET for x in ['condition','jour']):
    cdt = request.GET['condition']
    day = request.GET['jour']
    D = None
    min,moy,max = search_data(D,ctx,day)
    ctx = {'min':min,'moy':moy,'max':max}
    return render(request,'index.html',context=ctx)
return render(request,'index.html')
