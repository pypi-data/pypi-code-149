#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import Counter
import pandas as pd

class vizzy_doc:
    def __init__(self, data, column1, column2=None, column3=None, column4=None, column5=None):
        self.data = data
        self.column1 = column1
        self.column2 = column2
        self.column3 = column3
        self.column4 = column4
        self.column5 = column5
        
    def print_doc_stats(self):
        '''Print the statistics of your document'''
        def counter(data, column):
            return data[column].nunique()
            
        docs = max(idx for idx, other in self.data.iterrows())
        print("Here is your data summary:")
        print("\n")
        print("Total number of documents: {}".format(docs))
        print("Total number of {}: {}".format(str(self.column1), (counter(self.data, self.column1))))
        if self.column2 != None:
            print("Total number of {}: {}".format(str(self.column2), (counter(self.data, self.column2))))
        else:
            pass
        if self.column3 != None:
             print("Total number of {}: {}".format(str(self.column3), (counter(self.data, self.column3))))
        else:
            pass
        if self.column4 != None:
             print("Total number of {}: {}".format(str(self.column4), (counter(self.data, self.column4))))
        else:
            pass
        if self.column5 != None:
             print("Total number of {}: {}".format(str(self.column5), (counter(self.data, self.column5))))
        else:
            pass
    
    


# In[ ]:




