import os
from data import *


def ajouter_dans_liste_profils (profil):
    texte = "\n" + profil [0] + "," + profil [1] + ","+profil [2] + ","+profil [3] + ","+profil [4]
    with open("C:/Users/marti/OneDrive/Documents/Cours terminal/NSI/Projet_Tinder_MARTINKYRIANN-main/Projet_Tinder_MARTINKYRIANN-main/newdata.txt","a") as fichier:
        fichier.write(texte)
        fichier.close()

def creation_de_ton_profil():
    profil = []
    name= input ("Quel est le nom de ton personnage ?  ")
    profil.append (name)
    type = input("Quel est le type ethnique de ton personnage ? \
                réponds bien eurasien, africain, asiatique ou indien\
                                     ")
    while type not in authorized_types:
                 type = input ("Vous devez absolument choisir parmi ces types: eurasien, africain, asiatique ou indien: \
                    ")
    profil.append(type)

    physique = input("Quel est le physique de ton personnage ? \
                     réponds bien ectomorphe, endomorphe ou mesomorphe\
                                     ")
    while physique not in authorized_physiques:
                 physique = input("Vous devez absolument choisir parmi ces physiques : ectomorphe, endomorphe ou mesomorphe: \
                    ")

    profil.append(physique)
    style_musique = input("Quel est le type de musique préféré de ton personnage ? \
      réponds bien jazz, hardrock, rap, reggae ou salsa\
                                     ")
    while style_musique not in authorized_musiques :
                 style_musique = input("Vous devez absolument choisir parmi ces musiques : jazz, hardrock, rap, reggae ou salsa: \
                    ")
    profil.append(style_musique)
    caractere = input("Quel est le caractère de ton personnage ? \
                    réponds moyenne_ou_typique, reserve, role_modele ou centre_sur_soi)\
                                     ")
    while caractere not in authorized_caracteres :
          caractere = input("Vous devez absolument choisir parmi ces musiques : moyenne_ou_typique, reserve, role_modele ou centre_sur_soi: \
            ")
    profil.append(caractere)
    print("Votre profil a bien été enregistré dans notre base de données!")
    ajouter_dans_liste_profils (profil)

creation_de_ton_profil()


