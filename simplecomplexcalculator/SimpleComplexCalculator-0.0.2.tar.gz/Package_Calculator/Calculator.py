#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:34:10 2023

@author: tom.ebermeyer
"""


class SimpleComplexCalculator:
    """Classe de calcul pour nombres complexes"""

    def __init__(self, imag_1, imag_2):
        self.imag_1 = imag_1
        self.imag_2 = imag_2

    # Somme de nombres complexes
    def sum_imag(self):
        """Fonction somme"""
        if (
            (isinstance(self.imag_1[0], int))
                & (isinstance(self.imag_1[1], int))
                & (isinstance(self.imag_2[0], int))
                & (isinstance(self.imag_2[1], int))
        ):
            return (self.imag_1[0] + self.imag_2[0], self.imag_1[1] + self.imag_2[1])

        return "ERROR"

    # Difference de nombres complexes
    def sub_imag(self):
        """Fonction soustraction"""
        if (
            (isinstance(self.imag_1[0], int))
                & (isinstance(self.imag_1[1], int))
                & (isinstance(self.imag_2[0], int))
                & (isinstance(self.imag_2[1], int))
        ):
            return (self.imag_1[0] - self.imag_2[0], self.imag_1[1] - self.imag_2[1])
        
        return "ERROR"

    # Division de nombres complexes
    def div_imag(self):
        """Fonction division"""
        if (
            (isinstance(self.imag_1[0], int))
                & (isinstance(self.imag_1[1], int))
                & (isinstance(self.imag_2[0], int))
                & (isinstance(self.imag_2[1], int))
        ):
            div = self.imag_2[0] * self.imag_2[0] + self.imag_2[1] * self.imag_2[1]
            if div == 0:
                return "Cannot divide by zero ! "
            return (
                (self.imag_1[0] * self.imag_2[0] - self.imag_1[1] * (-self.imag_2[1]))
                / div,
                (self.imag_1[0] * (-self.imag_2[1]) + self.imag_1[1] * self.imag_2[0])
                / div,
            )
        return "ERROR"

    # Multiplication  de nombres complexes
    def mul_imag(self):
        """Fonction multiplication"""
        if (
            (isinstance(self.imag_1[0], int))
                & (isinstance(self.imag_1[1], int))
                & (isinstance(self.imag_2[0], int))
                & (isinstance(self.imag_2[1], int))
        ):
            return (
                self.imag_1[0] * self.imag_2[0] - self.imag_1[1] * self.imag_2[1],
                self.imag_1[0] * self.imag_2[1] + self.imag_1[1] * self.imag_2[0],
            )
        return "ERROR"
