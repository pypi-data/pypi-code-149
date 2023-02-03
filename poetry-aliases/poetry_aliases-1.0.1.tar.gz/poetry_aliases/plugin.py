import copy
from pathlib import Path

from cleo.events.console_command_event import ConsoleCommandEvent
from cleo.events.console_events import COMMAND
from poetry.config.config import Config
from poetry.console.application import Application
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_aliases.commands import PoetryAliasesCommand, PoetryAliasExecutor

here = Path(__file__).parent


class PoetryAliasesPlugin(ApplicationPlugin):
    def activate(self, application: Application) -> None:
        application.event_dispatcher.add_listener(COMMAND, interceptor)

        application.command_loader.register_factory(
            "aliases", PoetryAliasesCommand.factory()
        )

        for alias, command in Config.create().get("aliases", {}).items():
            if alias not in application.command_loader.names:
                application.command_loader.register_factory(
                    alias, PoetryAliasExecutor.factory(alias, command)
                )


def interceptor(event: ConsoleCommandEvent, *args, **kwargs):
    if isinstance(command := event.command, PoetryAliasExecutor):
        command.args = copy.copy(event.io.input._tokens[1:])
        event.io.input._tokens.clear()
