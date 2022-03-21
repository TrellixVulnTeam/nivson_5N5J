from django.shortcuts import render
from .td import *

# partie traitement des données


# partie requêtes

def index(request):
    return render(request, "index.html")

def cour_prem_arbre(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def cour_prem_casier(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def espace_fumeur(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def toilettes_prem(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def salle_cours(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def chapelle(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def salle_devoir_t(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def salle_devoir_p(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def couloir_prem(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def couloir_sd(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def couloir_ter(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def foyer(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def cdi(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def rest_cdi(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def rest_aquarium(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def refectoire(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def sport(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def cour_sd(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def preau_ter(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def ref_prof(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def sdp_pc(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def sdp_distrib(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')

def sdp_ref(request):
    ctx = request.GET('contexte')
    day = request.GET('jour')