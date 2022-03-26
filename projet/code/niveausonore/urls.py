# urls.py
# définit les urls des différentes pages ainsi que la requête qui doit être effectué (elles sont dans views.py)

"""niveausonore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [ # cette liste contient tout les chemins d'accès aux différentes pages
    path('',index,name='index'), # structure : chemin d'accès, requête, nom (pour les balises <a> dans les pages html)
    path('admin/', admin.site.urls),
    path('cour_prem_arbre',cour_prem_arbre,name='cour_prem_arbre'),
    path('cour_prem_casier',cour_prem_casier,name='cour_prem_casier'),
    path('espace_fumeur',espace_fumeur,name='espace_fumeur'),
    path('toilettes_prem',toilettes_prem,name='toilettes_prem'),
    path('salle_cours',salle_cours,name='salle_cours'),
    path('chapelle',chapelle,name='chapelle'),
    path('salle_devoir_t',salle_devoir_t,name='salle_devoir_t'),
    path('salle_devoir_p',salle_devoir_p,name='salle_devoir_p'),
    path('couloir_prem',couloir_prem,name='couloir_prem'),
    path('couloir_sd',couloir_sd,name='couloir_sd'),
    path('couloir_ter',couloir_ter,name='couloir_ter'),
    path('foyer',foyer,name='foyer'),
    path('cdi',cdi,name='cdi'),
    path('rest_cdi',rest_cdi,name='rest_cdi'),
    path('rest_aquarium',rest_aquarium,name='rest_aquarium'),
    path('refectoire',refectoire,name='refectoire'),
    path('sport',sport,name='sport'),
    path('cour_sd',cour_sd,name='cour_sd'),
    path('preau_ter',preau_ter,name='preau_ter'),
    path('ref_prof',ref_prof,name='ref_prof'),
    path('sdp_pc',sdp_pc,name='sdp_pc'),
    path('sdp_distrib',sdp_distrib,name='sdp_distrib'),
    path('sdp_ref',sdp_ref,name='sdp_ref'),

]
