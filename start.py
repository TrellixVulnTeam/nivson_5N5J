import re
import os
from os import fsync
import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def updating(filename,dico):

    RE = '(('+'|'.join(dico.keys())+')\s*=)[^\r\n]*?(\r?\n|\r)'
    pat = re.compile(RE)

    def jojo(mat,dic = dico ):
        return dic[mat.group(2)].join(mat.group(1,3))

    with open(filename,'r') as f:
        content = f.read()

    with open(filename,'w') as f:
        f.write(pat.sub(jojo,content))

vars = ['home']
new_values = [f" {os.path.abspath('projet/py')}"]
what_to_change = dict(zip(vars,new_values))
print(os.getcwd())
updating('projet/venv/pyvenv.cfg',what_to_change)

input('La configuration est terminé ! Ouvrez un terminal en mode administrateur et suivez les instructions :')
copy2clip(f"cd {os.path.abspath('projet/venv/Scripts')}")
input("collez et executez la commande qui se trouve dans votre presse-papiers, une fois l'étape terminé, appuyez sur entrée.")
copy2clip("activate")
input("collez et executez la commande qui se trouve dans votre presse-papiers, une fois l'étape terminé, appuyez sur entrée.")
copy2clip("cd ../../code")
input("collez et executez la commande qui se trouve dans votre presse-papiers, une fois l'étape terminé, appuyez sur entrée.")
copy2clip(f"{os.path.abspath('projet/venv/Scripts/python.exe')} manage.py runserver")
input("collez et executez la commande qui se trouve dans votre presse-papiers, une fois l'étape terminé, appuyez sur entrée.")
input("Vous pouvez maintenant suivre les instructions affichés à votre écran !")
