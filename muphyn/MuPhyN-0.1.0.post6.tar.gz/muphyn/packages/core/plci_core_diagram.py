#-----------------------------------
# Imports
#-----------------------------------

from typing import List, Dict

from .plci_core_box import Box
from .plci_core_signal import Signal

#-----------------------------------
# Class
#-----------------------------------

class Diagram :

    # -------------
    # Constructors
    # -------------
    def __init__ (self) :
        self._boxes : List[Box] = []
        self._signals : List[Signal] = []
        self._box_inputs : Dict[Signal, List[Box]] = {}
        self._linked_signals : Dict[Signal, List[Signal]] = {}
        self._inputs : List[int] = []
        self._outputs : List[int] = []

    # -------------
    # Properties
    # -------------

    @property
    def boxes (self) -> List[Box] :
        """Permet de récuperer les boxes dans le diagramme."""
        return self._boxes

    @property
    def signals (self) -> List[Signal] :
        """Permet de récuperer les signaux dans le diagramme."""
        return self._signals

    @property 
    def box_inputs (self) -> Dict[Signal, List[Box]] :
        """Permet de récuperer la liste des sigaux et les boites qui en dépendent."""
        return self._box_inputs

    @property
    def linked_signals (self) -> Dict[Signal, List[Signal]] :
        """Permet de récuperer la liste des connexions signaux entre le signaux."""
        return self._linked_signals

    @property
    def inputs (self) -> List[int] :
        """Permet de récuperer la liste des index des signaux d'entrées."""
        return self._inputs

    @property 
    def outputs (self) -> List[int] :
        """Permet de récuperer la liste des index des signaux de sorties."""
        return self._outputs

    # -------------
    # Methods
    # -------------

    def append (self, obj) -> None :
        """Permet d'ajouter un objet au diragramme."""

        if isinstance(obj, Diagram) :
            for box in obj.boxes :
                self._boxes.append(box)

            for signal in obj.signals :
                self._signals.append(signal)

            for signal in obj.box_inputs.keys() :
                self._box_inputs[signal] = obj.box_inputs[signal]

            for signal in obj._linked_signals.keys() :
                self._linked_signals[signal] = obj._linked_signals[signal]

        elif isinstance(obj, Box) :
            self.boxes.append(obj)

        elif isinstance(obj, Signal) :
            self.signals.append(obj)


    def add_box_inputs (self, box : Box, *signals : Signal) -> None :
        """Permet de lier des signaux comme entrée à une box."""
        
        signals_to_compute = []
        
        if not box in self._boxes :
            raise Exception(box, " not in diagram.")

        for signal in signals:

            if not signal in self._signals :
                raise Exception(signal, " not in diagram.")

            signals_to_compute.append(signal)

        for signal_to_compute in signals_to_compute :

            box.append_inputs(signal_to_compute)

            if not signal_to_compute in self._box_inputs:
                self._box_inputs[signal_to_compute] = []
            
            self._box_inputs[signal_to_compute].append(box)
        

    def add_box_outputs (self, box : Box, *signals : Signal) -> None :
        """Permet de lier des signaux comme sortie à une box."""

        signals_to_compute = []

        if not box in self._boxes :
            raise Exception(box, " not in diagram.")
            return

        for signal in signals:

            if not signal in self._signals :
                raise Exception(signal, " not in diagram.")

            signals_to_compute.append(signal)
                
        for signal_to_compute in signals_to_compute:
            box.append_outputs(signal_to_compute)
        
        
    def add_linked_signals (self, signal : Signal, *signals : Signal) -> None :
        """Permet de lier des signaux entre eux pour générer des modifications de valeurs en cascade."""

        signals_to_compute : List[Signal] = []

        if not signal in self._signals :
            Exception(signal, " not in diagram.")
            return

        for current_signal in signals:

            if not current_signal in self._signals :
                raise Exception(current_signal, " not in diagram.")
                
            signals_to_compute.append(current_signal)
            
        if not signal in self._linked_signals :
            self._linked_signals[signal] = []

        for signal_to_compute in signals_to_compute :
            self._linked_signals[signal].append(signal_to_compute)

        


        
