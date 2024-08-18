import random as rd
import csv
import os

NUMBER = 8
PATH = os.path.dirname(__file__)

#------------------------------------------------
# Affiche une liste d'élèves tirés au hasard
# Plus l'eleve a un poids elevé, plus il a de chances d'être choisi
# weight est un dictionnaire eleve -> poids
def pick_eleve(weights):
    sum_weights = sum(weights.values())
    pick = rd.random() * sum_weights
    index = 0
    val = list(weights.values())[index]
    while index < len(weights) and pick > val:
        index += 1
        val += list(weights.values())[index]
    return list(weights.keys())[index]

def random_eleves(weights):
    res = []
    for _ in range(NUMBER):
        eleve = pick_eleve(weights)
        res.append(eleve)
        weights.pop(eleve)
    return res

#------------------------------------------------
# Génère le dictionnaire des poids d'un élève en fonction de sa note
def gen_weights():
    with open(os.path.join(PATH,"Notes.csv")) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        rows = [row for row in reader][2:-1:]
    weights = {row[0] : len([i for i in row[1::] if i not in ["", "X"]]) for row in rows}
    max_weight = max(weights.values())
    weights = {eleve : max_weight + 1 - poids for eleve,poids in weights.items()}
    return weights

#------------------------------------------------
def main():
    weights = gen_weights()
    print(random_eleves(weights))
    
    

#------------------------------------------------
if __name__ == "__main__":
    main()