"""
This file is deprecated - MUST BE DELETED
"""

#-----------------------------------
# Class
#-----------------------------------

class Color :
    """Est le modèle de données pour les couleurs."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, red : float, green : float, blue : float) :

        self._red = red
        self._green = green
        self._blue = blue

    # -------------
    # Properties
    # -------------

    @property
    def red (self) -> float :
        """Permet de récuperer la valeur rouge de la couleur."""
        return self._red

    @property
    def green (self) -> float : 
        """Permet de récuperer la valeur verte de la couleur."""
        return self._green

    @property
    def blue (self) -> float : 
        """Permet de récuperer la valeur bleue de la couleur."""
        return self._blue

#-----------------------------------
# Static Elements
#-----------------------------------

black : Color = Color(0, 0,  0)
white : Color = Color(1, 1, 1)
gray_25 : Color = Color(0.25, 0.25, 0.25)
gray_50 : Color = Color(0.50, 0.50, 0.50)
gray_75 : Color = Color(0.75, 0.75, 0.75)
red : Color = Color(1, 0, 0)
green : Color = Color(0, 1, 0)
blue : Color = Color(0, 0, 1)
yellow : Color = Color(1, 1, 0)
cyan : Color = Color(0, 1, 1)
magenta : Color = Color(1, 0, 1)
