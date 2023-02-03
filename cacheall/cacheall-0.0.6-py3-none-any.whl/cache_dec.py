from cacheall.EvictionPolicies.LRUevictionpolicy import LRUCache
from cacheall.EvictionPolicies.LIFOevictionpolicy import LIFOCache
from cacheall.EvictionPolicies.FIFOevictionpolicy import FIFOCache
import threading

lock=threading.Lock()
cache=LRUCache(2,lock)
def cache_dec(func):
     
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    
    def inner1(*args):
        #making the key by concatinating the arguments into a string
        s=''
        for g in args:
            s+=str(g)
            s+='.'
        # print(s)
        
        #checking if the value is found in the cache or not
        k=0
        if cache.get(s)==-1:
            k=func(*args)
            cache.set(s,k)
        else:
            k=cache.get(s)
            print("value found in cache")
        
        return k
 
    return inner1