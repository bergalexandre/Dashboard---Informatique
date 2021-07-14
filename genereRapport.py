import subprocess
from datetime import datetime
import pandas
import os.path
from script.utils               import *
from script.HeuresTravaillees   import HeuresTravaillees
from script.TraceCourbeEnS      import CourbeEnS
from script.AvancementObjectifs import AvancementObjectifs
from script.AvancementSystemes  import AvancementSystemes
from script.Problemes           import Problemes
from script.TravailEffectue     import TravailEffectue
from PIL import Image

def run(*args):
    return subprocess.check_call(['git'] + list(args))


def dateActuel(Depart = "6/5/2021"):
    semaines = pandas.date_range(start=Depart, periods=16, freq="7D") #trimeste = 16 semaines????
    #trouve la semaine courante
    semaineN = 0
    for index, date in enumerate(semaines):
        if date > datetime.today():
            semaineN = index
            break
    return semaineN

def pull():
    run("pull")

#pas call pour le moment
def tagDernierRapportEtPushTag():
    run("tag", "-a", f"vSem{dateActuel()-1}")

def add(relativeFilePath):
    if(os.path.isfile(relativeFilePath) == False):
        raise Exception(f"Ton fichier existe pas {relativeFilePath}")
    run("add", relativeFilePath)

def commitEtPush():
    commit_message = f"\nCréation du template semaine{dateActuel()}"

    run("commit", "-m", commit_message)
    #run("push", "-u", "origin", "master")


# dimension est un tupple (x, y)
def resizePicture(path, dimension):
    img = Image.open(path)
    resized_img = img.resize(dimension)
    resized_img.save(path)



spec = Speciality.INFO
avancement_objectifs = AvancementObjectifs("DVP-Feuille-temps.xlsm")
avancement_objectifs.graphSave()

heures_travaillees = HeuresTravaillees(spec, offset=8)
heures_travaillees.fetchData()
heures_travaillees.graphSave()

CourbeEnS("DVP-Feuille-temps.xlsm")

taches_effectuees = TravailEffectue(spec)
taches_effectuees.fetchData()
taches_effectuees.graphSave()

#avancement_systemes = AvancementSystemes("DVP-Feuille-temps.xlsm", spec)
#avancement_systemes.fetchData()
#avancement_systemes.graphSave()

problemes = Problemes(spec)
problemes.fetchData()
problemes.graphSave()


resizePicture("img/progression_objectifs.png", (1336, 405))
resizePicture("img/avancement.png", (1185, 483))
resizePicture("img/Courbe_S.png", (604, 436))
resizePicture("img/heures_travaillees.png", (511, 342)) 

pull()
add("img/progression_objectifs.png")
add("img/avancement.png")
add("img/Courbe_S.png")
add("img/heures_travaillees.png")
add("img/taches")
add("img/problemes")
commitEtPush()

#budget = Budget(spec)
#budget.fetchData()
#budget.graphSave()