from feynmodel.base_class import BaseClass


class Coupling(BaseClass):

    require_args = ["name", "value", "order"]

    def __init__(self, name, value, order, **opt):

        args = (name, value, order)
        BaseClass.__init__(self, *args, **opt)
        #global all_couplings
        #all_couplings.append(self)
