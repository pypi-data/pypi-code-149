
from typing import TYPE_CHECKING
from .importer import transImporter
from .exporter import transExporter
import os

import re
if TYPE_CHECKING:
    from systemrdl.node import AddrmapNode
    from systemrdl import RDLCompiler, RDLCompileError

    import argparse
class MyImporterDescriptor:
    file_extensions = ["xlsx", "csv"]
    short_desc = "give a csv/xlxs file."
    long_desc = "..."

    def is_compatible(self, path: str) -> bool:
        # Could be any XML file.
        # See if file contains an ipxact or spirit component tag
        #with open(path, "r", encoding="utf-8") as f:
        #    if re.search(r"<(spirit|ipxact):component\b", f.read()):
        #        return True
        #return False
        pass
    
    def add_importer_arguments(self, arg_group: 'argparse.ArgumentParser') -> None:
        arg_group.add_argument("--xlsx", help="display a path of xlsx file", type=str)
        arg_group.add_argument("--csv", help="display a path of csv file", type=str)

    def do_import(self,  rdlc: 'RDLCompiler', options: 'argparse.Namespace') -> None:
        trans=transImporter()
        trans.import_file(options.xlsx)

class MyExporterDescriptor:
    short_desc = "transfer csv/xlxs  to rdl."
    def add_exporter_arguments(self, arg_group: 'argparse.ArgumentParser') -> None:
        pass

    def do_export(self,  top_node: 'AddrmapNode',options: 'argparse.Namespace') -> None:
        trans1=transExporter()
        trans1.export_file(options.output)
        
