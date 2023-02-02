#!/usr/bin/env python
# coding: utf-8
"""
author : Amaury CHRONOWSKI

"""

from numbers import Number


class SimpleComplexCalculator:
    """Cette classe a pour role de réaliser les opération arthimetique basique
    pour des nombres complexes (+, -, *, /)"""

    def isanumber(self, num):
        """Cette fonction vérifie si on a bien des nombre dans nos tuples. Et renvoi True si ils sont bien des nombres sinon False"""
        if isinstance(num[0], Number) and isinstance(num[1], Number) and not isinstance(num[0], bool) and not isinstance(num[1], bool):
            return True
        return False

    def add(self, num_1, num_2):
        """Cette fonction additionne 2 nombres complexes"""
        if not self.isanumber(num_1) or not self.isanumber(num_2):
            return "ERROR"

        res = (num_1[0] + num_2[0], num_1[1] + num_2[1])
        return res

    def sub(self, num_1, num_2):
        """Cette fonction soustrait 2 nombres complexes (num_1 - num_2)"""
        if not self.isanumber(num_1) or not self.isanumber(num_2):
            return "ERROR"

        res = (num_1[0] - num_2[0], num_1[1] - num_2[1])
        return res

    def mul(self, num_1, num_2):
        """Cette fonction multiplie 2 nombres complexes"""
        if not self.isanumber(num_1) or not self.isanumber(num_2):
            return "ERROR"

        res = (
            num_1[0] * num_2[0] - num_1[1] * num_2[1],
            num_1[1] * num_2[0] + num_2[1] * num_1[0],
        )
        return res

    def div(self, num_1, num_2):
        """Cette fonction divise 2 nombres complexes (num_1 / num_2).
        On mutiple le numérateur et le dénominateur par le conjugué du denominateur
        pour obtenir un nombre réel au dénominateur"""
        if (
            not self.isanumber(num_1)
            or not self.isanumber(num_2)
            or (num_2[0] == 0 and num_2[1] == 0)
        ):
            return "ERROR"

        temp = (num_2[0], -num_2[1])
        temp = self.mul(num_1, temp)
        res = (
            temp[0] / (num_2[0] * num_2[0] + num_2[1] * num_2[1]),
            temp[1] / (num_2[0] * num_2[0] + num_2[1] * num_2[1]),
        )
        return res
