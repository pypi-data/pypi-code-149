import sys 
import importlib
import os

from feynmodel.feyn_model import FeynModel
from feynmodel.particle import Particle
from feynmodel.vertex import Vertex


def ufo_object_to_dict(ufo_object):
    """Convert an UFO object to a dictionary"""
    return {key: ufo_object.__dict__[key] for key in ufo_object.require_args}


# Load a UFO model and convert it to a FeynModel object
def load_ufo_model(model_path, model_name="imported_ufo_model"):
    """Load a UFO model and convert it to a FeynModel object"""
    # Add the model path to the PYTHONPATH
    # This fixes the imports in the UFO model
    sys.path.append(os.path.abspath(model_path))
    # Madgraph workaround
    #os.environ["PYTHONPATH"] += os.pathsep + os.path.dirname(model_path)
    # Load the UFO model
    print("PYTHONPATH:", os.environ["PYTHONPATH"])
    spec = importlib.util.spec_from_file_location(model_name, os.path.abspath(model_path) + "/" + "__init__.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module 
    spec.loader.exec_module(module)
    model = module
    # model = importlib.import_module(os.path.abspath(model_path))

    # Convert the UFO model to a FeynModel object
    feynmodel = FeynModel()
    for particle in model.all_particles:
        feynmodel.add_particle(Particle(**ufo_object_to_dict(particle)))
    for vertex in model.all_vertices:
        feynmodel.add_vertex(Vertex(**ufo_object_to_dict(vertex)))
    return feynmodel
