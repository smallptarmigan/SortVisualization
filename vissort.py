# Sort Visualization

import array
import random
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

LISTNUM = 100
MIXNUM  = 200

# fixed seed value
random.seed(0)

def mix_data(array):
    for i in range(MIXNUM):
        a = random.randrange(LISTNUM)
        b = random.randrange(LISTNUM)
        array[a], array[b] = array[b], array[a]

def insertion_sort(array):
    count = 0
    n = len(array)
    for i in range(1,n):
        tmp = array[i]
        if tmp < array[i-1]:
            j = i
            while True:
                array[j] = array[j-1]
                j -= 1
                if j <= 0 or tmp >= array[j-1]:
                    break
            array[j] = tmp
        
        fig = plt.bar(range(len(array)), array, width=0.9)
        plt.savefig('./pic/image_{:0>6}.png'.format(count))
        #plt.show()
        plt.close('all')
        count += 1

if __name__ == '__main__':
    data = array.array('i', range(1, LISTNUM))
    mix_data(data)
    insertion_sort(data)


