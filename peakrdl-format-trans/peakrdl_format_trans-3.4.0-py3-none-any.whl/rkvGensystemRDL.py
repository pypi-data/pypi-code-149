
import re
import csv
import os
import argparse
from .format_translator import format_translator

class GensystemRDL:
    '''
    classdocs
    '''
    rdl_file = ''
    offset_addr_str = 'Offset address'
    field_bit_str = 'Bits'
    Field='Field'
    Field_access='Field_access'
    Reset_value='Reset_value'
    Function='Function'

    def __init__(self):
        '''
        Constructor
        '''
        self._rgmItemList = []
        self.systemRDLFileName = 'test.rdl'
        self.regblock_name = 'test'
        self.regblock_description = 'test V2.0'
        self._properties = {'register':  '', 'address':  '', 'fields': []}

    def readRgmFile(self, filename):
        "read register file and update the internal database"
        rgmFile = open(filename, 'r')
        reader = csv.DictReader(rgmFile)

        for infos in reader:
            if (infos[self.offset_addr_str] != ''):
                self._properties['register'] = infos[self.field_bit_str]
                self._properties['address'] = infos[self.offset_addr_str]
                self._rgmItemList.append(self._properties.copy())
                self._properties = {'register':  '', 'address':  '', 'fields': []}
                fieldInfos = {}

            if (infos[self.offset_addr_str] == ''):
                fieldInfos['field'] = infos[self.Field]
                fieldInfos['field_access'] = infos[self.Field_access]
                fieldInfos['reset_value'] = infos[self.Reset_value]
                fieldInfos['bits'] = infos[self.field_bit_str]
                fieldInfos['function'] = infos[self.Function]

                self._rgmItemList[-1]['fields'].append(fieldInfos)
                fieldInfos = {}




    def gensystemRDLFile(self,systemRDLFileName):
        with open(self.systemRDLFileName, 'w') as systemRDLFile:
            def _writeaddrmap():
                self.rdl_file = self.rdl_file + ('addrmap %s \n' % self.regblock_name)
                self.rdl_file = self.rdl_file + ('{\n')
                self.rdl_file = self.rdl_file + ('   name = "%s";\n' % self.regblock_name)
                self.rdl_file = self.rdl_file + ('   desc = "%s";\n' %self.regblock_description)
                self.rdl_file = self.rdl_file + ('   default regwidth = 32;\n' )
                self.rdl_file = self.rdl_file + ('   default hw=rw;\n')
                systemRDLFile.write(self.rdl_file )

            def _writeRegClass(properties_index):
                systemRDLFile.write('   reg %s {\n' % properties_index['register'])
                systemRDLFile.write('       name="%s";\n' %properties_index['register'])
                for fd in properties_index['fields']:
                    systemRDLFile.write('       field{\n')
                    if (fd['field_access'] == 'RO'):
                        systemRDLFile.write('           sw=r;\n')
                       # systemRDLFile.write('           onread=r;\n')
                    elif (fd['field_access'] == 'RC'):
                        systemRDLFile.write('           sw=r;\n')
                        systemRDLFile.write('           onread=rclr;\n')
                    elif (fd['field_access'] == 'RS'):
                        systemRDLFile.write('           sw=r;\n')
                        systemRDLFile.write('           onread=rset;\n')
                    elif (fd['field_access'] == 'WO'):
                        systemRDLFile.write('           sw=w;\n')
                      #  systemRDLFile.write('           onwrite=w;\n')
                    elif (fd['field_access'] == 'WOC'):
                        systemRDLFile.write('           sw=w;\n')
                        systemRDLFile.write('           onwrite=wclr;\n')
                    elif (fd['field_access'] == 'WOS'):
                        systemRDLFile.write('           sw=w;\n')
                        systemRDLFile.write('           onwrite=wset;\n')
                    elif (fd['field_access'] == 'WO1'):
                        systemRDLFile.write('           sw=w1;\n')
                     #   systemRDLFile.write('           onwrite=w;\n')
                    elif (fd['field_access'] == 'RW'):
                        systemRDLFile.write('           sw=rw;\n')
                      #  systemRDLFile.write('           onread=r;\n')
                     #   systemRDLFile.write('           onwrite=w;\n')
                    elif (fd['field_access'] == 'W1C'):
                        systemRDLFile.write('           sw=rw;\n')
                      #  systemRDLFile.write('           onread=r;\n')
                        systemRDLFile.write('           onwrite=woclr;\n')
                    elif (fd['field_access'] == 'W1S'):
                        systemRDLFile.write('           sw=rw;\n')
                    #    systemRDLFile.write('           onread=r;\n')
                        systemRDLFile.write('           onwrite=woset;\n')
                    elif (fd['field_access'] == 'W1T'):
                        systemRDLFile.write('           sw=rw;\n')
                    #    systemRDLFile.write('           onread=r;\n')
                        systemRDLFile.write('           onwrite=wot;\n')
                    elif (fd['field_access'] == 'W0C'):
                        systemRDLFile.write('           sw=rw;\n')
                     #   systemRDLFile.write('           onread=r;\n')
                        systemRDLFile.write('           onwrite=wzc;\n')
                    elif (fd['field_access'] == 'W0S'):
                        systemRDLFile.write('           sw=rw;\n')
                     #   systemRDLFile.write('           onread=r;\n')
                        systemRDLFile.write('           onwrite=wzs;\n')
                    elif (fd['field_access'] == 'W0T'):
                        systemRDLFile.write('           sw=rw;\n')
                     #   systemRDLFile.write('           onread=r;\n')
                        systemRDLFile.write('           onwrite=wzt;\n')
                    elif (fd['field_access'] == 'WC'):
                        systemRDLFile.write('           sw=rw;\n')
                    #    systemRDLFile.write('           onread=r;\n')
                        systemRDLFile.write('           onwrite=wclr;\n')
                    elif (fd['field_access'] == 'WS'):
                        systemRDLFile.write('           sw=rw;\n')
                    #    systemRDLFile.write('           onread=r;\n')
                        systemRDLFile.write('           onwrite=wset;\n')
                    elif (fd['field_access'] == 'WRC'):
                        systemRDLFile.write('           sw=rw;\n')
                        systemRDLFile.write('           onread=rclr;\n')
                    #    systemRDLFile.write('           onwrite=w;\n')
                    elif (fd['field_access'] == 'W1SRC'):
                        systemRDLFile.write('           sw=rw;\n')
                        systemRDLFile.write('           onread=rclr;\n')
                        systemRDLFile.write('           onwrite=woset;\n')
                    elif (fd['field_access'] == 'W0SRC'):
                        systemRDLFile.write('           sw=rw;\n')
                        systemRDLFile.write('           onread=rclr;\n')
                        systemRDLFile.write('           onwrite=wzs;\n')
                    elif (fd['field_access'] == 'WSRC'):
                        systemRDLFile.write('           sw=rw;\n')
                        systemRDLFile.write('           onread=rclr;\n')
                        systemRDLFile.write('           onwrite=wset;\n')
                    elif (fd['field_access'] == 'WRS'):
                        systemRDLFile.write('           sw=rw;\n')
                        systemRDLFile.write('           onread=rset;\n')
                     #   systemRDLFile.write('           onwrite=w;\n')
                    elif (fd['field_access'] == 'W1CRS'):
                        systemRDLFile.write('           sw=rw;\n')
                        systemRDLFile.write('           onread=rset;\n')
                        systemRDLFile.write('           onwrite=woclr;\n')
                    elif (fd['field_access'] == 'W0CRS'):
                        systemRDLFile.write('           sw=rw;\n')
                        systemRDLFile.write('           onread=rset;\n')
                        systemRDLFile.write('           onwrite=wzc;\n')
                    elif (fd['field_access'] == 'WCRS'):
                        systemRDLFile.write('           sw=rw;\n')
                        systemRDLFile.write('           onread=rset;\n')
                        systemRDLFile.write('           onwrite=wclr;\n')
                    elif (fd['field_access'] == 'W1'):
                        systemRDLFile.write('           sw=rw1;\n')
                    #    systemRDLFile.write('           onread=r;\n')
                    #    systemRDLFile.write('           onwrite=w;\n')
                    systemRDLFile.write('           desc="%s";\n' % fd['function'])
                    systemRDLFile.write('       }%s[%s]=%s;\n' % (
                        fd['field'], fd['bits'], fd['reset_value']))
                systemRDLFile.write('   };\n')

            def _writeRgmend():

                systemRDLFile.write('};\n')
            # gensystemRDLFile main function below
            _writeaddrmap()
            for properties_index in self._rgmItemList:
                _writeRegClass(properties_index)
            for properties_index in self._rgmItemList:
                systemRDLFile.write(
                '%s %s @ %s;\n' % (properties_index['register'], properties_index['register'], properties_index['address']))
            _writeRgmend()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-xlsx", help="display a path of csv file", type=str)
    parser.add_argument("-csv", help="display a path of csv file", type=str)
    args = parser.parse_args()
    format_trans=format_translator()
    if not os.path.exists(args.xlsx):
        print('%s \nEXCSL FILE PATH NOT EXISTS \n%s\n' % (40*'*', 40*'*'))
        print('ERROR')
        exit()
    print(args.xlsx)
  # if((args.csv==False)&&(args.xlsx)):
  #     print('%s \nXLSX TRANSFER TO RDL started \n%s\n' % (40 * '*', 40 * '*'))
  # if (args.csv == True && args.xlsx==False):
  #     print('%s \nCSV TRANSFER TO RDL started \n%s\n' % (40 * '*', 40 * '*'))
  # if (args.csv == False && args.xlsx==False):
  #     print('%s \n NO PARAMETER ARGS INPUT \n%s\n' % (40 * '*', 40 * '*'))
    if not os.path.exists(args.xlsx):
        print('%s \nEXCSL FILE PATH NOT EXISTS \n%s\n' % (40*'*', 40*'*'))
        print('ERROR')
        exit()
    print(args.xlsx)

    format_trans.XLSX2CSV(args.xlsx)
    print('%s \n transfer success \n%s' % (40*'*', 40*'*'))
    gen = GensystemRDL()
    gen.readRgmFile(format_trans.csv_name)
    gen.gensystemRDLFile(gen.systemRDLFileName)
    print('%s \ntransfer success \n%s' % (40*'*', 40*'*'))

