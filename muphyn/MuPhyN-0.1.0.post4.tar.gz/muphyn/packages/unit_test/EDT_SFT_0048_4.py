from os import system
import time


"""

Test to evaluate if sized queue works.




Au final, cette queue n'était pas utile et a été retirée.

"""
"""
sized_queue : SizedQueue[float] = SizedQueue(10)

_ = system('cls')
for i in range(30) :

    size = len(sized_queue)
    sized_queue.push(i)
    size_2 = len(sized_queue)

    _ = system('cls')
    print('adding', i, 'to the queue', size, 'then and', size_2, 'now')
    print('')
    print('queue : ')
    for i in sized_queue :
        print(i)

    time.sleep(0.5)
"""