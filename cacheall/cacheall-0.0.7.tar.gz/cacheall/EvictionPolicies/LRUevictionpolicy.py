from cacheall.Algorithms.doublylinkedlist import DoublyLinkedList as dll 
# LRU cache class
class LRUCache:

    def __init__(self, capacity,lock):
        # capacity: capacity of cache
        # Initialize all variable
        self.capacity = capacity
        self.map = {}
        self.list=dll()
        self.count = 0
        self.lock=lock


    # This method works in O(1)
    def get(self, key):
        with self.lock:
            if key in self.map:
                print("fetching",key)
                node = self.map[key]
                result = node.val
                self.list.deleteNode(node)
                self.map[key]=self.list.addToHead(key,result)
                print('Got the value : {} for the key: {}'.format(result, key))
                print("head of the list: ",self.list.head.key)
                # self.list.printlist()
                return result
            print('Did not get any value for the key: {}'.format(key))
            # self.list.printlist()
        return -1

    # This method works in O(1)
    def set(self, key, value):
        with self.lock:
            print('going to set the (key, value) : ( {}, {})'.format(key, value))
            if key in self.map:
                node = self.map[key]
                node.val = value
                self.list.deleteNode(node)
                self.map[key]=self.list.addToHead(key,value)
            else:
                if self.count < self.capacity:
                    self.count += 1
                    self.map[key]=self.list.addToHead(key,value)
                else:
                    del self.map[self.list.tail.key]
                    self.list.deleteNode(self.list.tail)
                    self.map[key]=self.list.addToHead(key,value)
            self.list.printlist()




