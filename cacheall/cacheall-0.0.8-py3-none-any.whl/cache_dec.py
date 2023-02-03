from EvictionPolicies.LRUevictionpolicy import LRUCache
from EvictionPolicies.LIFOevictionpolicy import LIFOCache
from EvictionPolicies.FIFOevictionpolicy import FIFOCache
import threading
import time

lock=threading.Lock()
dict={0:FIFOCache,1:LRUCache,2:LIFOCache}
def cache_dec(size,eviction,verbose=0):
    cache=dict[eviction](size,lock,verbose)
    def decorator(func):
    
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
            
            return k
 
        return inner1

    return decorator