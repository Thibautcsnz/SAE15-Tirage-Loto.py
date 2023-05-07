import numpy as np
from numpy import random
import csv
import matplotlib.pyplot as plt
import h5py
import array
import pickle
import array as arr
tab = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tab2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
i = 0
j = 0
nombre = 0
#Entrez une seed
graine = int(input("Entrez votre seed:"))

#Génère 5 nombres aléatoires entre 1 et 45 avec tirage sans remise (de 5 nombres)
tir=int(input("Entrez le nombre de tirages souhaité:"))
for i in range(tir):
    tableau = np.random.choice(range(1,45),5, replace=False)
    mylist = list(tableau)

    for j in range(45):
        nbr = mylist.count(j)
        tab[j] = (tab[j] + nbr)
        nbr=0

# Création d'un fichier csv, hdf5 et binaire met les données à l'intérieur
    with open('donnees.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow(mylist)

    with h5py.File('tableau_donnees', 'w') as f:
        tirage = f.create_dataset("tirage", data=tableau)

    with open('données.bin', 'wb') as f:
        pickle.dump(tab, f)

# Tri Cocktail
def tri_cocktail(tab):
    echange = True
    debut = 0
    fin = len(tab) - 2
    while echange:
        echange = False
        for i in range(0, len(tab) - 1):
            if tab[i] > tab[i + 1]:
                tab[i], tab[i + 1] = tab[i + 1], tab[i]
                echange = True
        for i in range(len(tab) - 2, -1, -1):
            if tab[i] > tab[i + 1]:
                tab[i], tab[i + 1] = tab[i + 1], tab[i]
                echange = True
    print(tab)

#Tri Fusion
def fusionner(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def tri_fusion(tableau):
    if len(tableau) <= 1:
        return tableau

    middle = len(tableau) // 2
    left = tri_fusion(tableau[:middle])
    right = tri_fusion(tableau[middle:])
    fu = fusionner(left, right)
    return fu

# Tri par insertion
def tri_insertion(tab):
    for i in range(1, len(tab)):
        k = tab[i]
        j = i - 1
        while j >= 0 and k < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
            tab[j + 1] = k
    print(tab)

#Création d'un histogramme :
plt.hist(tab2, bins=45, weights=tab, color='yellow', edgecolor = 'red')
plt.xlabel('Fréquence des valeurs')
plt.ylabel('Valeurs')
plt.title('Tirage Loto et fréquences des valeurs')
plt.show()

print(mylist)
#Choix du tirage
y=int(input("Choisissez votre tirage :"))
Tri = open('donnees.csv', 'r')
for i in range(y):
    Recherche = Tri.readline()
    tri = Recherche.split(" ")
    triage=[]
    i=0
    for i in range(5):
        triage.append(int(tri[i]))
print(triage)

#Recherche par dichotomie itératif
dichotomique = int(input("Quel nombre cherchez-vous dans la liste (dichotomie Itératif) ?: "))

def dichotomie(tab, x):
    left = 0
    right = len(tab) - 1

    while left <= right:
        mid = (left + right) // 2

        if tab[mid] == x:
            return mid
        elif tab[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = dichotomie(tab, dichotomique)
if result != -1:
    print(f"Le nombre {dichotomique} est présent à l'index {result}")
else:
    print(f"Le nombre {dichotomique} n'est pas présent dans le tableau")

#Recherche par dichotomie récursif

def dichotomie2(arr, x, left, right):
    tab = []
    num = int(input("Quel tirage (dichotomie récursive) ?: "))
    monfichier = open("donnees.csv", "r")

    for i in range(num):
        ligne = monfichier.readline()

    res = ligne.split(" ")

    for i in range(5):
        tab.append(int(res[i]))

    dichotomie2 = int(input("Quel nombre voulez vous rechercher (dichotomie récursive) ?: "))

    tri_insertion(tab)

    print(dichotomsuite(tab, dichotomie2, 0, len(tab) - 1))

def dichotomsuite(arr, x, left, right):
    if left > right:
        return print(f"Le nombre {dichotomique} n'est pas présent dans le tableau")

    mid = (left + right) // 2
    if arr[mid] == x:
        return print(f"Le nombre {dichotomique} est présent à l'index {result}")

    elif x < arr[mid]:
        return dichotomsuite(arr, x, left, mid - 1)

    else:
        return dichotomsuite(arr, x, mid + 1, right)
dichotomie2(tab, dichotomique, 0, len(tab)-1)

#Choix mode de tri
n=int(input("Choisissez votre mode de Tri : \n1 : Tri Cocktail \n2 : Tri Fusion \n3 : Tri par Insertion\n"))

if n==1:
   tri_cocktail(triage)
elif n==2:
    print(tri_fusion(triage))
elif n==3:
    tri_insertion(triage)