#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 16:06:51 2023

@author: benoit.jomain
"""


class Simple_Complex_Calculator:
    "Classe qui gère les opérations de nombres complexes"
    def __init__(self, t_1, t_2):
        self.t_1 = t_1
        self.t_2 = t_2

    def somme_imag(self):
        "Fonction somme imaginaire"
        return self.t_1[0] + self.t_2[0], self.t_1[1] + self.t_2[1]

    def difference_imag(self):
        "Fonction différence imaginaire"
        return self.t_1[0] - self.t_2[0], self.t_1[1] - self.t_2[1]

    def multiplication_imag(self):
        "Fonction multiplication imaginaire"
        return (
            self.t_1[0] * self.t_2[0] - self.t_1[1] * self.t_2[1],
            self.t_1[0] * self.t_2[1] + self.t_1[1] * self.t_2[0],
        )

    def division_imag(self):
        "Fonction division imaginaire"
        diviseur = self.t_2[0] ** 2 + self.t_2[1] ** 2
        return (self.t_1[0] * self.t_2[0] - self.t_1[1] * (-self.t_2[1])) / diviseur, (
            self.t_1[0] * (-self.t_2[1]) + self.t_1[1] * self.t_2[0]
        ) / diviseur


if __name__ == "__main__":
    CALCUL = Simple_Complex_Calculator((3, 2), (5, 4))
    print(CALCUL.difference_imag())
    print(CALCUL.division_imag())
    print(CALCUL.somme_imag())
    print(CALCUL.multiplication_imag())
