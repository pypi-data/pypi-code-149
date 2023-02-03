"""Run `aiida-shell` through an OTE strategy. Store (and refer to) results in the AiiDA database."""
# pylint: disable=too-few-public-methods
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from aiida.orm import Data
from oteapi.models import AttrDict, FunctionConfig, SessionUpdate
from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from execflow.utils import run_aiida_shell


class AiidaShellConfig(AttrDict):
    """AiidaShellStrategy-specific configuration."""

    aiida_profile: Optional[str] = Field(
        None,
        description=(
            "The AiiDA profile to load and use. If `None` is given (default), the "
            "default profile will be loaded."
        ),
    )
    executable: Path = Field(
        ..., description="Executable program or script to launch with aiida-shell."
    )
    filenames: Optional[Dict[str, str]] = Field(
        None,
        description=(
            "Dictionary of explicit filenames to use for the `nodes` to be written to "
            "`dirpath`."
        ),
    )
    nodes: Optional[Dict[str, Union[str, Path, Data]]] = Field(
        None,
        description=(
            "A dictionary of AiiDA Data nodes whose content is to replace "
            "placeholders in the 'arguments' list."
        ),
    )
    arguments: Optional[List[str]] = Field(
        None,
        description=(
            "List of command line arguments optionally containing placeholders for "
            'input nodes. Example: `["--quiet", "{input_file}"]`.'
        ),
    )
    outputs: Optional[List[str]] = Field(
        None,
        description="List of relative filenames that should be captured as outputs.",
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description=(
            "Dictionary of metadata inputs to be passed to the AiiDA Shell "
            "calculation job."
        ),
    )
    run_async: bool = Field(
        False,
        description=(
            "Whether or not to submit the job to an AiiDA Daemon worker in a "
            "sub-process or run it directly in the current process."
        ),
    )

    @validator("executable", allow_reuse=True)
    def executable_exists(cls, value: Path) -> Path:  # pylint: disable=no-self-argument
        """Ensure the executable exists.

        Parameters:
            value: The parsed value for `executable`.

        Returns:
            The resolved (absolute) path to the executable.

        """
        executable = value.resolve()
        if not executable.exists():
            raise FileNotFoundError(f"{executable} not found !")
        return executable


class AiidaShellFunctionConfig(FunctionConfig):
    """AiidaShellStrategy function config."""

    functionType: str = Field(
        "aiida_shell",
        const=True,
        description=FunctionConfig.__fields__["functionType"].field_info.description,
    )
    configuration: AiidaShellConfig = Field(
        ..., description="AiiDA-Shell function strategy-specific configuration."
    )


class AiidaShellSession(SessionUpdate):
    """AiidaShellStrategy session update class."""

    results: Dict[str, str] = Field(
        ...,
        description=(
            "Results dictionary when run non-async. The dictionary contains AiiDA "
            "output labels as keys and Node UUIDs as values."
        ),
    )
    job_node_uuid: str = Field(
        ..., description="The AiiDA ProcessNode representing the AiiDA Shell job."
    )


@dataclass
class AiidaShellStrategy:
    """Strategy for running `aiida-shell` synchronously.

    **Registers strategies**:

    - `("functionType", "aiida_shell")`

    """

    function_config: AiidaShellFunctionConfig

    def initialize(
        self,
        session: "Optional[Dict[str, Any]]" = None,  # pylint: disable=unused-argument
    ) -> SessionUpdate:
        """Initialize strategy.

        This method can be called through the `/initialize` endpoint of the OTEAPI
        Services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        return SessionUpdate()

    def get(
        self,
        session: "Optional[Dict[str, Any]]" = None,  # pylint: disable=unused-argument
    ) -> AiidaShellSession:
        """Execute the strategy.

        This method can be called through the strategy-specific endpoint of the
        OTEAPI Services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        results, node = run_aiida_shell(self.function_config.configuration)

        return AiidaShellSession(
            results={label: node.uuid for label, node in results.items()},
            job_node_uuid=node.uuid,
        )
