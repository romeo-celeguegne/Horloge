# importer l'heure
import time
# importer l'heure et la date depuis le fichier datetime
from datetime import datetime


def heure_actuelle():  # afficher l'heure actuelle
    while True:  # tant que rien ne stop la boucle, rajouter une seconde
        heure = str(datetime.now().time())
        heure = heure[:-7]
        print(heure)
        time.sleep(1)


def afficher_heure():  # définir une heure précise
    heure_modifier = (16, 30, 0)  # choisir l'heure
    heure = heure_modifier[0]  # définir l'affichage de l'heure
    minute = heure_modifier[1]
    secondes = heure_modifier[2]
    while True:  # tant que rien ne stop la boucle, avancer dans l'heure
        secondes = secondes + 1
        if secondes == 60:
            secondes = 0
            minute = minute + 1
        if minute == 60:
            minute = 0
            heure = heure + 1
        if heure == 24:
            heure = 0

        heure = str(heure)  # passer en chaine de caractère (string)
        minute = str(minute)
        secondes = str(secondes)
        if len(secondes) < 2:
            secondes = list(secondes)
            secondes.insert(0, "0")
            secondes = "".join(secondes)
        if len(minute) < 2:
            minutes = list(minute)
            minutes.insert(0, "0")
            minutes = "".join(minute)
        if len(heure) < 2:
            heure = list(heure)
            heure.insert(0, "0")
            heure = "".join(heure)

        # afficher l'heure dans le bon format
        print(heure+":"+minute+":"+secondes)
        heure = int(heure)
        minute = int(minute)
        secondes = int(secondes)
        time.sleep(1)  # la fonction se repose une seconde


def alarme():  # définir une alarme
    while True:  # tant que l'heure de reveil n'apparait pas, continuer la boucle
        heure = str(datetime.now().time())
        heure = heure[:-7]
        reveil = "10:20:00"  # choisir l'heure de reveil
        if reveil == heure:
            print("Reveil toi fréro")
            break
        else:
            time.sleep(1)

# heure_actuelle()
# afficher_heure()
# alarme()
