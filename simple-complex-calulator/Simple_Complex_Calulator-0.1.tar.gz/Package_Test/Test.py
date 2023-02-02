#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:43:40 2023

@author: benoit.jomain
"""
import unittest
import logging
from Package_Calculator import calculator as cal

class Test_Calculator_Operation(unittest.TestCase):
    """Classe de test qui vérifie les différentes opérations"""

    def setUp(self):
        """ Insanciation de la classe"""
        self.calcul = cal.Simple_Complex_Calculator((12, 10), (9, 7))
        self.log = logging.getLogger()

    def test_somme_imag(self):
        """Test de la méthode somme_imag"""
        res = self.calcul.somme_imag()
        self.assertEqual(res, (21, 17))
        self.log.info("La somme marche")

    def test_difference_imag(self):
        """Test de la méthode difference_imag"""
        res = self.calcul.difference_imag()
        self.assertEqual(res, (3, 3))
        self.log.info("La difference marche")

    def test_multiplication_imag(self):
        """Test de la méthode multiplication_imag"""
        res = self.calcul.multiplication_imag()
        self.assertEqual(res, (38, 174))
        self.log.info("La multiplication marche")

    def test_division_imag(self):
        """Test de la méthode division_imag"""
        res = self.calcul.division_imag()
        self.assertEqual(res, (1.3692307692307693, 0.046153846153846156))
        self.log.info("La division marche")

class Test_Calculator_float(unittest.TestCase):
    """Classe qui teste si les entrées pour chaque méthode sont bien des entiers"""
    def setUp(self):
        """Insanciation de la classe"""
        self.calcul = cal.Simple_Complex_Calculator((12.1, 10.1), (9.1, 7.23))
        self.log = logging.getLogger()

    def test_somme_imag(self):
        """Test de la méthode somme_imag pour savoir si les entrées sont des entiers"""
        res = self.calcul.somme_imag()
        self.assertEqual(res, "ERROR")
        self.log.warning("Vous n'entrez pas des entiers")

    def test_difference_imag(self):
        """Test de la méthode difference_imag pour savoir si les entrées sont des entiers"""
        res = self.calcul.difference_imag()
        self.assertEqual(res, "ERROR")
        self.log.warning("Vous n'entrez pas des entiers")

    def test_multiplication_imag(self):
        """Test de la méthode muliplication_imag pour savoir si les entrées sont des entiers"""
        res = self.calcul.multiplication_imag()
        self.assertEqual(res, "ERROR")
        self.log.warning("Vous n'entrez pas des entiers")

    def test_division_imag(self):
        """Test de la méthode division_imag pour savoir si les entrées sont des entiers"""
        res = self.calcul.division_imag()
        self.assertEqual(res, "ERROR")
        self.log.warning("Vous n'entrez pas des entiers")

class Test_Calculator_Division_Zero(unittest.TestCase):
    """Classe qui teste que la division par  renvoie ERROR"""

    def setUp(self):
        """Insanciation de la classe"""
        self.calcul = cal.Simple_Complex_Calculator((12.1, 10.1), (0, 0.0))
        self.log = logging.getLogger()

    def test_division_imag(self):
        """Test de la division par 0"""
        res = self.calcul.division_imag()
        self.assertEqual(res, "ERROR")
        self.log.error("Vous ne pouvrez pas diviser par 0")

if __name__ == '__main__':
    unittest.main()
