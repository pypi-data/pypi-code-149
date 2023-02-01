from iman import *
import re


def normal(filename ,file_out=None, replist= "c:\\Replace_List.txt"):

   mwords=[]
   words=[]
   ph=[]
   with open(replist , encoding='utf-8') as fr:
      for line in fr:
          t = line.split('\t')
          mwords.append(t[0])
          words.append(t[1])
          ph.append(t[2].strip())
                  
   def repwords(_str):
     for i in range(len(words)):
       if (words[i] in _str):
           pattern = "(^|\s)" + words[i] + "($|\s)"
           _str = re.sub(pattern ," " + mwords[i] + " " ,  _str)
       if (ph[i] in _str):
           pattern = "(^|\s)" + ph[i] + "($|\s)"
           _str = re.sub(pattern ," " + mwords[i] + " " ,  _str)
     return(_str.strip())
   
   matn  = Read(filename)

   if (file_out==None):
       file_out= PN(filename) + '_normal' + PE(filename)
   fid = open(file_out , 'w',encoding='utf-8')
   fid.write(repwords(matn)) 
   fid.close()    
