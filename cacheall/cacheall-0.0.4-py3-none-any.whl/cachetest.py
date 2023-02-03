from EvictionPolicies.LRUevictionpolicy import LRUCache
from EvictionPolicies.FIFOevictionpolicy import FIFOCache
from EvictionPolicies.LIFOevictionpolicy import LIFOCache
import threading
from threading import Thread


def threadf1(lock):
    print('Going to test the LRU Cache Implementation')
    cache = FIFOCache(2,lock)
    cache.set(1, 10)
    cache.set(2, 20)
    print('Value for the key: 1 is {}'.format(cache.get(1))) 
    cache.set(3, 30)
    print('Value for the key: 2 is {}'.format(
    cache.get(2)))
    cache.set(4, 40)
    print('Value for the key: 1 is {}'.format(
    cache.get(1))) 
    print('Thread 1:Value for the key: 7 is {}'.format(cache.get(7))) 
    print('Value for the key: 4 is {}'.format(cache.get(4)))

def threadf2(lock):
    print('Going to test the LRU Cache Implementation')
    cache = FIFOCache(2,lock)
    cache.set(5, 10)
    cache.set(7, 20)
    cache.set(9,18)
    print('Thread2:value of 5 {}'.format(cache.get(5)))
    print('Thread2:value of 7 {}'.format(cache.get(7)))
    print('Thread2:value of 9 {}'.format(cache.get(9)))

mylock=threading.Lock() 

#now the cache is thread safe
t1=Thread(target=threadf1,args=(mylock,))
t2=Thread(target=threadf2,args=(mylock,))

t1.start()
t2.start()

t1.join()
t2.join()