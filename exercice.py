#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
from recettes import add_recipes, print_recipe
from os import path
import json
# TODO: Définissez vos fonction ici
def trouver_diff(chemin_fichier1, chemin_fichier2):
    with open(chemin_fichier1) as f1, open(chemin_fichier2) as f2:
        liste1, liste2 = f1.readlines(), f2.readlines()
    f1.close(), f2.close()
    with open(chemin_fichier1) as f1, open(chemin_fichier2) as f2:
        for i in range(len(liste1)):
            ligne1 = liste1[i]
            ligne2 = liste2[i]
            if ligne1 != ligne2:
                print('Les deux fichiers ne sont pas pareils.')
                print(ligne1)
                print("N'est pas pareil que")
                print(ligne2)
                return
        print('Les deux fichiers sont identiques')

def fichier_espace_triple(chemin_fichier):
    with open(chemin_fichier) as f1 , open('fichier_triple', mode='w') as f2:
        lignes_f1 = f1.readlines()
        for ligne in lignes_f1:
            liste=ligne.split()
            nouvelle_ligne = ""
            for element in liste:
                nouvelle_ligne += (element+'   ')
            f2.write(nouvelle_ligne + '\n')

def note_to_grade(chemin_fichier):
    with open(chemin_fichier) as f1, open('notes_lettres.txt', mode='w') as f2:
        liste_notes = f1.readlines()
        for note in liste_notes:
            for cle, tranche in PERCENTAGE_TO_LETTER.items():
                if tranche[0] <= int(note) < tranche[1]:
                    f2.write(note.strip()+' '+cle+'\n')
                    break

def supprimer_recette(livre_recette):
    recette = input('Veuillez entrer la recette à supprimer\n')
    if recette in livre_recette:
        del livre_recette[recette]
        print(f'La recette {recette} a été supprimée')
    else:
        print('La recette n\' est pas dans le livre de recette')
    return livre_recette

def creer_livre_recettes(chemin_recette):
    if path.exists(chemin_recette):
        with open(chemin_recette, encoding="utf-8") as livre:
            recettes = json.load(livre)
    else:
        recettes = dict()
    while True:
        action = input("Que voulez-vous faire? \n a) Ajouter une recette \n b) Modifier une recette \n c) Supprimer une recette \n d) Afficher une recette \n e) Quitter le programme\n").strip()
        if action == 'a':
            recettes = add_recipes(recettes)
        elif action == 'b':
            recettes = add_recipes(recettes)
        elif action == 'c':
            recettes = supprimer_recette(recettes)
        elif action == 'd':
            print_recipe(recettes)
        elif action == 'e':
            break
        else:
            print('Cette action n\'est pas possible')
    with open(chemin_recette, 'w', encoding="utf-8") as livre:
        json.dump(recettes, livre)

def return_numbers(chemin_fichier):
    with open(chemin_fichier) as f:
        lignes = f.readlines()
    liste_num = []
    for ligne in lignes:
        for element in ligne.split():
            if element.isnumeric():
                liste_num.append(int(element))
    return sorted(liste_num)

def recopie1sur2(chemin_fichier, chemin_copie):
    with open(chemin_fichier, 'r') as f1, open(chemin_copie, 'w') as f2:
        lignes = f1.readlines()
        print(lignes)
        print(len(lignes))
        for i in range(0, len(lignes), 2):
            f2.write(lignes[i])


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    diff = trouver_diff('exemple.txt', 'exemple.txt')
    fichier_espace_triple('exemple.txt')
    note_to_grade('notes.txt')
    #creer_livre_recettes('livre_recettes.json')
    return_numbers('exemple.txt')
    recopie1sur2('exemple.txt', 'copie1sur2.txt')