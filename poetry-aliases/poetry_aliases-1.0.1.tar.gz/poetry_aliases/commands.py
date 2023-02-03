import subprocess
import textwrap
from abc import ABC, abstractmethod
from typing import Self

import click
import tomlkit as toml
from poetry.config.config import Config
from poetry.console.commands.command import Command


class _PoetryCommand(Command, ABC):
    @abstractmethod
    def factory(self, *args, **kwargs) -> Self:
        ...


class PoetryAliasesCommand(_PoetryCommand):
    name = "aliases"
    description = "View or edit your aliases."

    def handle(self) -> int:
        msg = f"""
        # Write each alias on a separate line, e.g.:

        # i = "install"
        # r = "remove"
        # dev = "add --group dev"
        # plugins = "self show plugins"
        
        # Aliases that are not strings or conflict with other Poetry commands will be ignored.
        
        # Save this file and close the editor when you're done.
        
        """
        new_aliases = click.edit(
            textwrap.dedent(msg).lstrip()
            + toml.dumps(Config.create().get("aliases", {})),
            extension=".toml",
            require_save=True,
        )
        if new_aliases:
            self.poetry.config.config_source.add_property(
                "aliases", toml.parse(new_aliases)
            )

    @classmethod
    def factory(cls) -> Self:
        def wrapper():
            return cls()

        return wrapper


class PoetryAliasExecutor(_PoetryCommand):
    hidden = True

    def __init__(self, alias: str, command: str):
        super().__init__()
        self.name = alias
        self.command = command
        self.args = []

    def handle(self) -> int:
        subprocess.run(["poetry", *self.command.split(), *self.args])

    @classmethod
    def factory(cls, alias: str, command: str) -> Self:
        def wrapper():
            return cls(alias, command)

        return wrapper
