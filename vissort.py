# Sort Visualization

import sys
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

def make_image(array, count):
    #plt.bar(range(len(array)), array, width=0.95)
    plt.bar(range(len(array)), array)
    plt.xlim([-1,len(array)])
    plt.tick_params(labelbottom="off",bottom="off")
    plt.tick_params(labelleft="off",left="off")
    plt.savefig('./pic/image_{:0>6}.png'.format(count))
    #plt.show()
    plt.close('all')

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
        make_image(array, count)
        #sys.exit()
        count += 1

if __name__ == '__main__':
    data = array.array('i', range(1, LISTNUM))
    mix_data(data)
    insertion_sort(data)


