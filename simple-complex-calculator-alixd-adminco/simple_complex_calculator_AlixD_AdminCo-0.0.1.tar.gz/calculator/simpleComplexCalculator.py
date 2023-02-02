#!/usr/bin/env python
# coding: utf-8

import logging
from numbers import Number

"""
@author: Alix Deleule

Ce module comprend la classe SimpleComplexCalculator 
et permet de tester les differentes fonctions de cette classe 
en appelant en tant que main.
"""


class SimpleComplexCalculator:
    """
    Cette classe permet d'efffectuer des operations mathematiques simples
    avec des nombres complexes.
    """

    def isNbTuple(self, x):
        """
        La fonction vérifiant que les 2 éléments du tuple soit des nombres(int ou float).

        Parameters:
            x ( tuple(2) ) : nombre complexe

        Returns:
            boolean : True si les 2 éléments sont des nombres False sinon.
        """
        ret = (
            isinstance(x[0], Number)
            and isinstance(x[1], Number)
            and not isinstance(x[0], bool)
            and not isinstance(x[1], bool)
        )
        if ret:
            logging.info("is a tuple of 2 numbers")
        else:
            logging.info("is NOT a tuple of 2 numbers")
        return ret

    def conjugue(self, x):
        """
        La fonction permettant d'obtenir le conjugué d'un nombre complexe.

        Parameters:
            x ( tuple(2) ) : nombre complexe

        Returns:
            tuple(2) : Un nombre complexe conjugué du paramètre.
        """
        if self.isNbTuple(x):
            ret = (x[0], -x[1])
            logging.info("Conjugate of %s completed successfuly.", str(ret))
            return ret
        else:
            logging.error("x has NOT a correct value : %s", str(x))
            raise ValueError("x should be a tuple(2) of numbers")

    def sum(self, x, y):
        """
        La fonction permettant d'obtenir la somme de 2 nombres complexes.

        Parameters:
            x ( tuple(2) ) : nombre complexe
            y ( tuple(2) ) : nombre complexe

        Returns:
            tuple(2) : Un nombre complexe somme des 2 paramètres.
        """
        if self.isNbTuple(x) and self.isNbTuple(y):
            ret = (x[0] + y[0], x[1] + y[1])
            logging.info("Addition completed successfuly.")
            return ret
        else:
            logging.error("x has NOT a correct value : %s or %s", str(x), str(y))
            raise ValueError("x and y should be tuple(2) of numbers")

    def substract(self, x, y):
        """
        La fonction permettant d'obtenir la soustraction de 2 nombres complexes.

        Parameters:
            x ( tuple(2) ) : nombre complexe
            y ( tuple(2) ) : nombre complexe

        Returns:
            tuple(2) : Un nombre complexe soustraction des 2 paramètres.
        """
        if self.isNbTuple(x) and self.isNbTuple(y):
            ret = (x[0] - y[0], x[1] - y[1])
            logging.info("Substraction completed successfuly.")
            return ret
        else:
            logging.error("x has NOT a correct value : %s or %s", str(x), str(y))
            raise ValueError("x and y should be tuple(2) of numbers")

    def multiply(self, x, y):
        """
        La fonction permettant d'obtenir la multiplication de 2 nombres complexes.

        Parameters:
            x ( tuple(2) ) : nombre complexe
            y ( tuple(2) ) : nombre complexe

        Returns:
            tuple(2) : Un nombre complexe multiplication des 2 paramètres.
        """
        if self.isNbTuple(x) and self.isNbTuple(y):
            ret = (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
            logging.info("Multiplication completed successfuly.")
            return ret
        else:
            logging.error("x has NOT a correct value : %s or %s", str(x), str(y))
            raise ValueError("x and y should be tuple(2) of numbers")

    def divide(self, x, y):
        """
        La fonction permettant d'obtenir la division de 2 nombres complexes.

        Parameters:
            x ( tuple(2) ) : nombre complexe
            y ( tuple(2) ) : nombre complexe

        Returns:
            tuple(2) : Un nombre complexe division des 2 paramètres.
        """
        if self.isNbTuple(x) and self.isNbTuple(y):
            if y[0] == 0 and y[1] == 0:
                logging.error("Cannot divide by zero : %s", str(y))
                raise ZeroDivisionError("Cannot divide by zero")
            y_c = self.conjugue(y)
            a = self.multiply(x, y_c)
            logging.info("Division completed successfuly.")
            return tuple(ti / self.multiply(y, y_c)[0] for ti in a)
        else:
            logging.error("x has NOT a correct value : %s or %s", str(x), str(y))
            raise ValueError("x and y should be tuple(2) of numbers")


if __name__ == "__main__":
    a = (1, 2)
    b = (0, 0)
    calculator = SimpleComplexCalculator()
    sm = calculator.sum(a, b)
    print("x + y = " + str(sm))
    sb = calculator.substract(a, b)
    print("x - y = " + str(sb))
    m = calculator.multiply(a, b)
    print("x * y = " + str(m))
    d = calculator.divide(a, b)
    print("x / y = " + str(d))
