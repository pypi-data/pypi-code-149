from cacheall.Algorithms.doublylinkedlist import DoublyLinkedList as dll 

class Verbose:

    def __init__(self, verbose=0):
        self.verbose=verbose
        self.list=dll()

    
    def get_data(self,key,value,head):
        if self.verbose>0:
            if value==-1:
                print("Did'nt find any value for {}".format(key))
            else:
                print('Got the value : {} for the key: {}'.format(value, key))
        if self.verbose==2:
            self.list.printlist(head)

    def set_data(self,key,value,head=None):
        if self.verbose>0:
            print("({}, {}) added to cache".format(key,value))
        if self.verbose==2:
            self.list.printlist(head)
            




