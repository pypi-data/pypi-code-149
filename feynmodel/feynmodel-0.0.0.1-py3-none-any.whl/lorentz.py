from feynmodel.base_class import BaseClass


class Lorentz(BaseClass):

    require_args = ["name", "spins", "structure"]

    def __init__(self, name, spins, structure="external", **opt):
        args = (name, spins, structure)
        BaseClass.__init__(self, *args, **opt)

        #global all_lorentz
        #all_lorentz.append(self)
