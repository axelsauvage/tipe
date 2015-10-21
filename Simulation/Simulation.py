# coding: utf8

from Route import *


class Simulation(object):

    def __init__(self):
        self.temps = 60.0 # Durée de la simulation en secondes
        self.delta = 1/60.0 # Intervalle de temps entre chaque calcul
        self.route = Route()

    def parametres(self):
        pass

    def initialisation(self):
        self.route.initialisation()

    def lancer(self):
        self.initialisation()

        temps_total = 0
        while temps_total < self.temps:
            self.route.update(self.delta, temps_total)
            temps_total += self.delta

        self.route.afficher_force(0)
        self.route.afficher_force(1)
        self.route.afficher(0, self.temps, -3200, 3200)

s = Simulation()
s.lancer()
