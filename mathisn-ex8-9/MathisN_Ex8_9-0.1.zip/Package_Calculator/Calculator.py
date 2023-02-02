# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:26:07 2023

@author: mathi
"""


class SimpleComplexCalculator:
    "Classe qui effectue les 4 opérations pour 2 imaginaires"

    def __init__(self, imaginaire_1, imaginaire_2):
        self.imaginaire_1 = imaginaire_1
        self.imaginaire_2 = imaginaire_2

    def sum_imaginaire(self):
        "Fonction qui somme 2 imaginaires(représentés par des tuples de 2 nombres)"
        if list(map(type, self.imaginaire_1)) == [int, int] and list(
                map(type, self.imaginaire_2)
        ) == [int, int]:
            return (
                self.imaginaire_1[0] + self.imaginaire_2[0],
                self.imaginaire_1[1] + self.imaginaire_2[1],
            )
        return "ERROR"

    def substract_maginaire(self):
        "Fonction qui soustrait 2 imaginaires(représentés par des tuples de 2 nombres)"
        if list(map(type, self.imaginaire_1)) == [int, int] and list(
                map(type, self.imaginaire_2)
        ) == [int, int]:
            return (
                self.imaginaire_1[0] - self.imaginaire_2[0],
                self.imaginaire_1[1] - self.imaginaire_2[1],
            )
        return "ERROR"

    def division_imaginaire(self):
        "Fonction qui divise 2 imaginaires(représentés par des tuples de 2 nombres)"
        if list(map(type, self.imaginaire_1)) == [int, int] and list(
                map(type, self.imaginaire_2)
        ) == [int, int]:
            diviseur = self.imaginaire_2[0] ** 2 + self.imaginaire_2[1] ** 2
            if diviseur == 0:
                return "On ne peut pas diviser par 0"
            return (
                (
                    self.imaginaire_1[0] * self.imaginaire_2[0]
                    - self.imaginaire_1[1] * (-self.imaginaire_2[1])
                )
                / diviseur,
                (
                    self.imaginaire_1[0] * (-self.imaginaire_2[1])
                    + self.imaginaire_1[1] * self.imaginaire_2[0]
                )
                / diviseur,
            )
        return "ERROR"

    def multiplication_imaginaire(self):
        "fonction qui multplie 2 imaginaires(représentés par des tuples de 2 nombres)"
        if list(map(type, self.imaginaire_1)) == [int, int] and list(
                map(type, self.imaginaire_2)
        ) == [int, int]:
            return (
                self.imaginaire_1[0] * self.imaginaire_2[0]
                - self.imaginaire_1[1] * self.imaginaire_2[1],
                self.imaginaire_1[0] * self.imaginaire_2[1]
                + self.imaginaire_1[1] * self.imaginaire_2[0],
            )
        return "ERROR"
