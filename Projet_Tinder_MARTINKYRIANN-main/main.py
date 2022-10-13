from data import *


datapretendants=readdata()
pretendants=[ligne[1:] for ligne in datapretendants]
pretendants_nom=[ligne[0] for ligne in datapretendants]
#profile de l'user et ses préférences

user = ["africain","endomorphe","rap","reserve"]
print(pretendants)
pref_ethnie=input("rentrez votre préférence de type de votre partenaire idéal:")
while pref_ethnie not in authorized_types:
                 pref_ethnie = input ("Vous devez absolument choisir parmi ces types: eurasien, africain, asiatique ou indien: \
                    ")
pref_corps=input("rentrez votre préférence de physique de votre partenaire idéal :")
while pref_corps not in authorized_physiques:
                 pref_corps = input("Vous devez absolument choisir parmi ces physiques : ectomorphe, endomorphe ou mesomorphe: \
                    ")
pref_musique=input("rentrez votre préférence pour les goûts musicaux de votre partenaire idéal :")
while pref_musique not in authorized_musiques :
                 pref_musique = input("Vous devez absolument choisir parmi ces styles  de musique : jazz, hardrock, rap, reggae ou salsa: \
                    ")
pref_caractere=input("rentrez votre préférence de caractere pour votre partenaire :")
while pref_caractere not in authorized_caracteres :
          pref_caractere = input("Vous devez absolument choisir parmi ces musiques : moyenne_ou_typique, reserve, role_modele ou centre_sur_soi: \
            ")

user_preferences = [pref_ethnie,pref_corps,pref_musique,pref_caractere]

#comparer les préférences avec les prétendants ave la fonction match

## a faire: annoncer les 3 plus compatibles 
#elus=[]
elus={}
amour=[]
def match(user_preferences, pretendants):

    for i in range(0,len(pretendants)):
        compatibilite = 0
        for j in range(4):
            if user_preferences[j]== pretendants[i][j]:
                compatibilite = compatibilite + 1
            else:
                compatibilite=compatibilite
        compatibilite= compatibilite*25
        #elus.append(compatibilite)
        elus[pretendants_nom[i]]=compatibilite


def trois_plus_compatibles(elus):
    #elus.sort(reverse=True)
    elus2 = {key: val for key, val in sorted(elus.items(), key = lambda ele: ele[1], reverse = True)}
    #elus=elus(sorted(elus.items(),key= lambda x:x[1]))
    print("Vous êtes le plus compatible avec:")
    for x in list(elus2)[0:3]:
        print (str(x) + " à " + str(elus[x]) + "%")








match (user_preferences, pretendants)
trois_plus_compatibles(elus)