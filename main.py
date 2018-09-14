# Sort Visualization main function

import sys
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
    print("[log] complete mix array")
        
if __name__ == '__main__':
    start = time.time()

    data = array.array('i', range(1, LISTNUM))
    mix_data(data)

    try :
        args = sys.argv
        if args[1] == "-i":
            sort.insertion_sort(data)
        elif args[1] == "-b":
            sort.bubble_sort(data)
        elif args[1] == "-s":
            sort.selection_sort(data)
        elif args[1] == "-m":
            sort.merge_sort(data)
        elif args[1] == "-q":
            sort.quick_sort(data)
        elif args[1] == "-r":
            sort.radix_sort(data)
        else:
            sys.exit("[error] select option")
    except :
        sys.exit("[error] select option")

    print("[runtime] {0}[s]".format(time.time() - start))

