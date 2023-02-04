from feynmodel.base_class import BaseClass


class FormFactor(BaseClass):
    require_args = ["name", "type", "value"]

    def __init__(self, name, type, value, **opt):
        args = (name, type, value)
        BaseClass.__init__(self, *args, **opt)

        #global all_form_factors
        #all_form_factors.append(self)
