# coding: utf8

from Simulation import Simulation
from math import exp
import cProfile


def gaussienne(x):
    return 0.06*(exp(-0.00001*(x-500)**2)*0.5 + 0.1)


def feux_rouges(x):
    if x <= 1000:
        return 0.07
    else:
        return 0


def constante(x):
    return 0.02

s = Simulation.Simulation(150, 1/20.0)
s.route.ajouter_section(2000, 25)

resultat = s.initialisation(gaussienne, affichage=False)
if resultat:
    # s.analyse = True
    s.route.desactiver_flux_densite()
    s.route.boucle = True
    s.sauvegarde = False

    # cProfile.run('s.lancer()')
    s.lancer()
