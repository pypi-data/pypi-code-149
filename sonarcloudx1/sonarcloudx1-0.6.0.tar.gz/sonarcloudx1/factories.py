import factory
from .project import Project
from .components import Components

class ProjectFactory(factory.Factory):
    
    class Meta:
        model = Project
        
    personal_access_token = None
    sonar_url = None

class ComponentsFactory(factory.Factory):
    
    class Meta:
        model = Components

    personal_access_token = None
    sonar_url = None

