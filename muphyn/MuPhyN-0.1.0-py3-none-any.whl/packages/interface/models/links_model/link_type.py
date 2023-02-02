#-----------------------------------
# Import
#-----------------------------------

from enum import Enum
    
#-----------------------------------
# Class
#-----------------------------------

class LinkType(Enum) : 
    """Est l'énumeration qui reprends les différents mode de méthode de dessin des signaux."""

    SQUARE = 0,
    """Est le mode de lien où les signaux doivent décrire des angles droits."""

    CURVED = 1
    """Est le mode de lien où les signaux doivent décrire des courbes."""

    def __str__ (self) -> str :

        if self == LinkType.SQUARE :
            return 'SQUARE'

        else :
            return 'CURVED'
    
    
#-----------------------------------
# Methods
#-----------------------------------

def get_link_type (link_type : str) -> LinkType :

    if link_type == 'SQUARE' :
        return LinkType.SQUARE

    else :
        return LinkType.CURVED