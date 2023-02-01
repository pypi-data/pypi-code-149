#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import Counter
import seaborn as sns

class vizzy_token:
    def __init__(self, data, column):
        self.data = data
        self.column = column
        
    def show_labels_count(self):
        '''show count of each label'''
        labels = self.data[self.column]
        counter = Counter(labels)
        x = list(counter.keys())
        y = list(counter.values())
        plot = sns.barplot(x=y,y=x)
        return plot
    
    def print_labels_count(self):
        '''print count of each label'''
        labels = self.data[self.column]
        counter = Counter(labels)
        x = list(counter.keys())
        y = list(counter.values())
        z = zip(x,y)
        for label, count in z:
            print("Total number of {}: {}".format(label, count))


# In[ ]:




