from cpanlp.event.acquisition.acquisition import *

class HostileAcquisition(Acquisition):
    def __init__(self, target_company, acquiring_company,acquisition_ratio,hostile_tactic=None,price=None):
        super().__init__(target_company, acquiring_company, acquisition_ratio, price)
        self.hostile_tactic = hostile_tactic