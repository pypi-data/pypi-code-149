
# coding = utf-8
import os
import pandas as pd
import csv
from openpyxl import load_workbook

class format_translator:
    csv_name='test.csv'
    def XLSX2CSV(self,data_filenamepath):
        """
        转换 xlsx -> csv
        :param data_filenamepath: xlsx 文件路径
        :return: csv 文件路径
        """
        def get_filename(path_filename):
            """
            获取文件所在文件夹路径、带拓展文件名、文件名、拓展名
            :param path_filename: 带拓展完整路径
            :return: 文件所在文件夹路径、带拓展文件名、文件名、拓展名
            """
            (filepath, tempfilename) = os.path.split(path_filename)
            (filename, extension) = os.path.splitext(tempfilename)
            return filepath, tempfilename, filename, extension
        filepath, tempfilename, filename, extension = get_filename(data_filenamepath)
        sheet = load_workbook(data_filenamepath).worksheets[0]
        rows = list(sheet.rows)
        print('********a')
        print(rows)
        sheet_val = []
        for row in rows:
            row_val = [col.value for col in row]
            sheet_val.append(row_val)
        print("excle表格转化csv", sheet_val[0])
        dt = pd.DataFrame(sheet_val[1:len(sheet_val)-1], columns=sheet_val[0])
        save_dir = './'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        CSVfilepath = os.path.join(save_dir, self.csv_name)
        print('aaa'+CSVfilepath)
        dt.to_csv(CSVfilepath, index=0)
        return CSVfilepath
if __name__ == '__main__':
    format_trans=format_translator()
    format_trans.XLSX2CSV('test_excel.xlsx')