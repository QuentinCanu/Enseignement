import networkx as nx
import matplotlib.pyplot as plt

Reseau = nx.Graph()
options = {}

def ajouterPersonne(nom):
    Reseau.add_node(nom)

def ajouterAmitie(nom1, nom2):
    Reseau.add_edge(nom1,nom2)

def reinitialiser():
    global Reseau
    Reseau = nx.Graph()

def dessinerReseau():
    plt.plot()
    nx.draw(Reseau, **options)
    plt.show()