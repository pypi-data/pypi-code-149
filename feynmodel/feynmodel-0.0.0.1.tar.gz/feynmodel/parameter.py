from feynmodel.base_class import BaseClass


class Parameter(BaseClass):

    require_args = ["name", "nature", "type", "value", "texname"]

    def __init__(self, name, nature, type, value, texname, lhablock=None, lhacode=None):

        args = (name, nature, type, value, texname)

        BaseClass.__init__(self, *args)

        args = (name, nature, type, value, texname)

        #global all_parameters
        #all_parameters.append(self)

        if (lhablock is None or lhacode is None) and nature == "external":
            raise Exception('Need LHA information for external parameter "%s".' % name)
        self.lhablock = lhablock
        self.lhacode = lhacode
