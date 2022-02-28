from django.shortcuts import render
from datetime import datetime 

# partie traitement des données

temps = datetime.now()
heure = f'{temps.hour} : {temps.minute}'

# partie requêtes

def index(request):
    return render(request, "index.html",context={'heure':heure})