from .format_translator import format_translator
from .rkvGensystemRDL import GensystemRDL
import os
from systemrdl import RDLCompiler
class transImporter():

    def __init__(self, compiler: RDLCompiler):
        """
        Parameters
        ----------
        """



    def import_file(self,xlsx_name) -> None:
        """
        Import a single SPIRIT or IP-XACT file into the SystemRDL namespace.

        Parameters
        ----------
        path:
            Input SPIRIT or IP-XACT XML file.
        remap_state:
            Optional remapState string that is used to select memoryRemap regions
            that are tagged under a specific remap state.
        """
        format_trans=format_translator()
        if not os.path.exists(xlsx_name):
            print('%s \nEXCSL FILE PATH NOT EXISTS \n%s\n' % (40*'*', 40*'*'))
            print('ERROR')
            exit()
       #if not os.path.exists(csv_name):
       #    print('%s \nEXCSL FILE PATH NOT EXISTS \n%s\n' % (40*'*', 40*'*'))
       #    print('ERROR')
       #    exit()
        print(xlsx_name)
        format_trans.XLSX2CSV(xlsx_name)


    