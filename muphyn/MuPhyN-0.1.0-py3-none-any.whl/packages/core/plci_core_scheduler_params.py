#-----------------------------------
# Imports
#-----------------------------------

#-----------------------------------
# Class
#-----------------------------------

class SchedulerParams :
    """Est la classe qui permet de maintenir les paramètres de la simulation dans une classe."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, stop_time_ : float = 10.0, step_time_ : float = 0.1) :
        self._stop_time = stop_time_
        self._step_time = step_time_

    # -------------
    # Properties
    # -------------

    @property 
    def step_time (self) -> float : 
        """Permet de récuperer le pas de temps pour la simulation."""
        return self._step_time

    @property 
    def stop_time (self) -> float :
        """Permet de récuperer le temps de fin de simulation."""
        return self._stop_time
