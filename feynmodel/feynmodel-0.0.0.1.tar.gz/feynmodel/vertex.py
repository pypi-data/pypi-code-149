from feynmodel.base_class import BaseClass


class Vertex(BaseClass):

    require_args = ["name", "particles", "color", "lorentz", "couplings"]

    def __init__(self, name, particles, color, lorentz, couplings, **opt):

        args = (name, particles, color, lorentz, couplings)

        BaseClass.__init__(self, *args, **opt)

        args = (particles, color, lorentz, couplings)

        #global all_vertices
        #all_vertices.append(self)
