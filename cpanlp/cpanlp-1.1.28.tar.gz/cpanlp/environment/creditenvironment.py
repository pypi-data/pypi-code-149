from cpanlp.environment.economicenvironment import *

class CreditEnvironment(EconomicEnvironment):
    def __init__(self):
        super().__init__()
        self.add_factor("interest_rate", 0)
        self.add_factor("default_rate", 0)