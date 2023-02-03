import re

class NameList:
    """Class that holds a list of all possible Toon Name entries."""
    def __init__(self,titles:list=[],firsts:list=[],last1s:list=[],last2s:list=[]):
        self.title = titles
        self.first = firsts
        self.last1 = last1s
        self.last2 = last2s
    def from_file(path:str):
        file = open(path,'r')
        text = file.readlines()
        file.close()
        title = []
        first = []
        last1 = []
        last2 = []
        for line in text:
            txt = line.split("*", 2)
            if re.search('^[0-9]{1,4}[*]0[*]',line):
                title.append(txt[2].strip())
                continue
            elif re.search('^[0-9]{1,4}[*]1[*]',line):
                first.append(txt[2].strip())
                continue
            elif re.search('^[0-9]{1,4}[*][2-3][*]',line):
                last1.append(txt[2].strip())
                continue
            elif re.search('^[0-9]{1,4}[*]4[*]',line):
                last2.append(txt[2].strip())
                continue
            else:
                continue
        return NameList(title,first,last1,last2)