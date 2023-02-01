from .component_metadata import ComponentMetadata
from .experiment_metadata import ExperimentMetadata
from .run_definition import RunDefinition
from .run_history import RunHistory

all_tables = [
    ComponentMetadata.__table__,
    ExperimentMetadata.__table__,
    RunDefinition.__table__,
    RunHistory.__table__,
]