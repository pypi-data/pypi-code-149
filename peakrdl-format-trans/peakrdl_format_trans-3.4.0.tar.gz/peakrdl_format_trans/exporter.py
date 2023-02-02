
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

    


    def export_file(self,rdlname) -> None:
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
        print('%s \n transfer success \n%s' % (40*'*', 40*'*'))
        gen = GensystemRDL()
        gen.readRgmFile(format_trans.csv_name)
        #outpath=outdir+rdlname
        gen.gensystemRDLFile(rdlname)
        print('%s \ntransfer success \n%s' % (40*'*', 40*'*'))

    