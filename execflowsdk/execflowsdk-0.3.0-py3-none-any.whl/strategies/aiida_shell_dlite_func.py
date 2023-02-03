"""Run `aiida-shell` through an OTE strategy. Store (and refer to) results as a DLite collection."""
# pylint: disable=too-few-public-methods
from copy import deepcopy
from tempfile import NamedTemporaryFile
from typing import Any, Dict, Optional

import dlite
from oteapi.models import FunctionConfig
from oteapi_dlite.models import DLiteSessionUpdate
from oteapi_dlite.strategies.parse import DLiteParseConfig
from oteapi_dlite.utils import get_collection, update_collection
from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from execflow.strategies.aiida_shell_func import AiidaShellConfig, AiidaShellSession
from execflow.utils import run_aiida_shell


class AiidaShellDliteConfig(AiidaShellConfig):
    """AiidaShellDliteStrategy-specific configuration."""

    outputs: Optional[Dict[str, DLiteParseConfig]] = Field(  # type: ignore[assignment]
        None,
        description="List of relative filenames that should be captured as outputs.",
    )

    @validator("outputs", pre=True)
    def autogenerate_label(  # pylint: disable=no-self-argument
        cls, value: "Dict[str, Dict[str, Any]]"
    ) -> "Dict[str, Dict[str, Any]]":
        """Auto-generated 'label' for `DLiteParseConfig`, if not defined."""
        result = deepcopy(value)
        for output_label, parse_config_entry in value.items():
            if not parse_config_entry.get("label"):
                result[output_label]["label"] = output_label
        return result


class AiidaShellDliteFunctionConfig(FunctionConfig):
    """AiidaShellStrategy function config."""

    functionType: str = Field(
        "aiida_shell_dlite",
        const=True,
        description=FunctionConfig.__fields__["functionType"].field_info.description,
    )
    configuration: AiidaShellDliteConfig = Field(
        ..., description="AiiDA-Shell DLite function strategy-specific configuration."
    )


class AiidaShellDliteSession(AiidaShellSession, DLiteSessionUpdate):
    """Combination of `aiida_shell` and oteapi-dlite update sessions."""


@dataclass
class AiidaShellDliteStrategy:
    """Strategy for running `aiida-shell` synchronously using DLite.

    The DLite aspect governs the outputs - as they will be stored in a DLite
    Collection.

    **Registers strategies**:

    - `("functionType", "aiida_shell_dlite")`

    """

    function_config: AiidaShellDliteFunctionConfig

    def initialize(
        self,
        session: "Optional[Dict[str, Any]]" = None,
    ) -> DLiteSessionUpdate:
        """Initialize strategy.

        This method can be called through the `/initialize` endpoint of the OTEAPI
        Services.

        Initialize a DLite Collection if it does not already exist, storing it in the
        session-specific context from services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        return DLiteSessionUpdate(collection_id=get_collection(session).uuid)

    def get(
        self,
        session: "Optional[Dict[str, Any]]" = None,
    ) -> DLiteSessionUpdate:
        """Execute the strategy.

        This method can be called through the strategy-specific endpoint of the
        OTEAPI Services.

        Loads an AiiDA profile and runs `launch_shell_job()` from AiiDA-Shell.
        Then ensures the outputs are parsed using DLite and stored in the DLite
        Collection, whose UUID should be found in the session - if not, it will be
        created.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        config = self.function_config.configuration

        results, node = run_aiida_shell(config)

        if results and config.outputs:
            coll = get_collection(session)
            for default_label, dlite_config in config.outputs.items():
                with NamedTemporaryFile(mode="w+t") as handle:
                    handle.write(results[default_label.replace(".", "_")].get_content())
                    handle.seek(0)

                    inst = dlite.Instance.from_location(
                        driver=dlite_config.driver,
                        location=handle.name,
                        options=dlite_config.options,
                        id=dlite_config.id,
                    )

                    coll.add(
                        dlite_config.label
                        if dlite_config.label is not None
                        else default_label,
                        inst,
                    )
            update_collection(coll)

        return AiidaShellDliteSession(
            collection_id=coll.uuid,
            results={label: node.uuid for label, node in results.items()},
            job_node_uuid=node.uuid,
        )
