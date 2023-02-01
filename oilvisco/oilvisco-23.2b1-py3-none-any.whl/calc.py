"""
Library for calculation functions.
"""

from .datatypes import Oil, OilPart
from functools import reduce


def mix(oil1, oil2):
    """
    takes two partial values
    returns a OilPartial
    """
    (v1, u1) = oil1
    (v2, u2) = oil2
    return OilPart((v1*u1+v2*u2 )/ (u1+u2), u1+u2)



def blend(oils):
    """
    takes an iterable of Oil-Structures and calculates the blended viscosities.
    returns Oil
    """

    for n, oil in enumerate(oils):
        if n == 0:
            lastlower = OilPart(oil.lower, oil.liter)
            lastupper = OilPart(oil.upper, oil.liter)
            continue

        lastlower = mix(OilPart(oil.lower, oil.liter), lastlower)
        lastupper = mix(OilPart(oil.upper, oil.liter), lastupper)

    return Oil(lastlower.value, lastupper.value, sum((oil.liter for oil in oils)))
