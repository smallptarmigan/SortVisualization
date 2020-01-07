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

    args = sys.argv
    if len(args) < 2:
        sys.exit("[error] select option")

    if args[1] == "-in":
        sort.insertion_sort(data)
    elif args[1] == "-bu":
        sort.bubble_sort(data)
    elif args[1] == "-se":
        sort.selection_sort(data)
    elif args[1] == "-me":
        sort.merge_sort(data)
    elif args[1] == "-qu":
        sort.quick_sort(data)
    elif args[1] == "-lsd":
        sort.lsd_radix_sort(data)
    elif args[1] == "-msd":
        sort.msd_radix_sort(data)
    elif args[1] == "-sh":
        sort.shell_sort(data)
    elif args[1] == "-sk":
        sort.shaker_sort(data)
    elif args[1] == "-he":
        sort.heap_sort(data)
    elif args[1] == "-cm":
        sort.comb_sort(data)
    elif args[1] == "-oe":
        sort.oddeven_sort(data)
    elif args[1] == "-gn":
        sort.gnome_sort(data)
    elif args[1] == "-gr":
        sort.gravity_sort(data)
    elif args[1] == "-st":
        print("[log] reset array")
        data = array.array('i', range(1, 30))
        mix_data(data)
        sort.stooge_sort(data)
    else:
        sys.exit("[error] select option")

    print("[log] {0}[s]".format(time.time() - start))

