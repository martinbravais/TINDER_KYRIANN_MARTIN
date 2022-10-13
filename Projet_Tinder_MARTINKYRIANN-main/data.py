# Créé par bravais, le 16/09/2022 en Python 3.7

repertoire = "C:/Users/marti/OneDrive/Documents/Cours terminal/NSI/Projet_Tinder_MARTINKYRIANN-main/Projet_Tinder_MARTINKYRIANN-main"


authorized_types = ["eurasien", "africain", "asiatique", "indien"]
authorized_physiques =  ["ectomorphe", "endomorphe", "mesomorphe"]
authorized_musiques = ["jazz", "hardrock", "rap", "reggae", "salsa"]
authorized_caracteres = ["moyenne_ou_typique", "reserve", "role_modele" , "centre_sur_soi"]



nomfichier='/newdata.txt'
#nomfichier='data_profil.txt'
longueurliste=5

def readdata():
  "Lis le fichier data_profil.txt"
  with open (repertoire + nomfichier,'r') as fichier:
     s = fichier.read ()
  datapretendants=[]
  for ligne in s.split("\n"):
    l = ligne.split(",")
    if len(l) == longueurliste:
      datapretendants.append(l)

  return datapretendants

def writedata(profil):
    texte = "\n" + ",".join(profil)
    with open (repertoire + nomfichier,'a') as fichier:
        fichier.write (texte)