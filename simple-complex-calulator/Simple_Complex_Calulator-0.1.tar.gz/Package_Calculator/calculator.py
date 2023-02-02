#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:58:19 2023

@author: benoit.jomain
"""
class Simple_Complex_Calculator:
    """Classe qui gère les opérations de nombres complexes où un nombre complexe est un tuple : (a,b) où a est la partie réelle et b la partie imaginaire  """
    def __init__(self, t_1, t_2):
        self.t_1 = t_1
        self.t_2 = t_2

    def somme_imag(self):
        """Fonction qui somme 2 nombres complexes"""
        if self.Verif_Entree_Saisi() == True :
            return self.t_1[0] + self.t_2[0], self.t_1[1] + self.t_2[1]
        return "ERROR"

    def difference_imag(self):
        """Fonction qui fait la différence entre 2 nombres imaginaires (t1 - t2)"""
        if self.Verif_Entree_Saisi() == True :
            return self.t_1[0] - self.t_2[0], self.t_1[1] - self.t_2[1]
        return "ERROR"

    def multiplication_imag(self):
        """Fonction qui multiplit 2 nombres imaginaires"""
        if self.Verif_Entree_Saisi() == True :
            return (
                self.t_1[0] * self.t_2[0] - self.t_1[1] * self.t_2[1],
                self.t_1[0] * self.t_2[1] + self.t_1[1] * self.t_2[0],
            )
        return "ERROR"

    def division_imag(self):
        """Fonction qui divise 2 nombres imaginaires (t1/t2)"""
        if self.Verif_Entree_Saisi() == True and (self.t_2[0] and self.t_2[1]) != 0 :
            diviseur = self.t_2[0] ** 2 + self.t_2[1] ** 2
            return (self.t_1[0] * self.t_2[0] - self.t_1[1] * (-self.t_2[1])) / diviseur, (
                self.t_1[0] * (-self.t_2[1]) + self.t_1[1] * self.t_2[0]
            ) / diviseur
        if (self.t_2[0] and self.t_2[1]) == 0 : 
            print("Vous ne pouvez pas diviser par 0")
        return "ERROR"
        
    def Verif_Entree_Saisi(self):
        if isinstance(self.t_1[0], int) and isinstance(self.t_1[1], int) and isinstance(self.t_2[0], int) and isinstance(self.t_2[1], int) :
            print("Entrées validées")
            return True
        print("Erreur")
        return "ERROR"