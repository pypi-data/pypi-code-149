
from .rkvGensystemRDL import GensystemRDL
from .format_translator import format_translator
import os
from systemrdl import RDLCompiler
class transExporter():

    def __init__(self,):
        """
        Parameters
        ----------
        """

    


    def export_file(self,xlsx_name,rdlname,) -> None:
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
        print('%s \n transfer success \n%s' % (40*'*', 40*'*'))
        gen = GensystemRDL()
        print(format_trans.csv_name)
        gen.readRgmFile(format_trans.csv_name)
        #outpath=outdir+rdlname
        gen.gensystemRDLFile(rdlname)
        print('aaa')
        print(rdlname)
        print('%s \ntransfer success \n%s' % (40*'*', 40*'*'))

    