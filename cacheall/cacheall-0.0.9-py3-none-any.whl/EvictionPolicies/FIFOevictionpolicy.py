from cacheall.Algorithms.doublylinkedlist import DoublyLinkedList as dll 
from cacheall.EvicitonPolicies.verbose import Verbose
# LRU cache class
class FIFOCache:

    def __init__(self, capacity,lock,verbose=0):
        # capacity: capacity of cache
        # Initialize all variable
        self.capacity = capacity
        self.map = {}
        self.verdata=Verbose(verbose)
        self.verbose=verbose
        self.list=dll()
        self.count = 0
        self.lock=lock


    # This method works in O(1)
    def get(self, key):
        with self.lock:
            result=-1
            if key in self.map:
                node = self.map[key]
                result = node.val
            self.verdata.get_data(key,result,self.list.head)
            return result

    # This method works in O(1)
    def set(self, key, value):
        with self.lock:
            if key in self.map:
                node = self.map[key]
                node.val = value
            else:
                if self.count < self.capacity:
                    self.count += 1
                    self.map[key]=self.list.addToHead(key,value)
                else:
                    del self.map[self.list.tail.key]
                    self.list.deleteNode(self.list.tail)
                    self.map[key]=self.list.addToHead(key,value)
            self.verdata.set_data(key,value,self.list.head)


