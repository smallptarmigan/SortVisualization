# Sort Visualization main function

import time
import array
import random
import numpy as np

import sort

LISTNUM = 50
MIXNUM  = 300

# fixed seed value
random.seed(0)

def mix_data(array):
    for i in range(MIXNUM):
        a = random.randrange(len(array))
        b = random.randrange(len(array))
        array[a], array[b] = array[b], array[a]
    print("complete mix array")
        
if __name__ == '__main__':
    start = time.time()

    data = array.array('i', range(1, LISTNUM))
    mix_data(data)

    #sort.insertion_sort(data)
    #sort.bubble_sort(data)
    #sort.selection_sort(data)
    sort.merge_sort(data)

    print(time.time() - start)

