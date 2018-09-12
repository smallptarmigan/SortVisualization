# Sort Visualization

import sys
import time
import array
import random
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

LISTNUM = 50
MIXNUM  = 300

# fixed seed value
random.seed(0)

def make_image(array, count, m, a, b):
    fig, ax = plt.subplots(1,1)
    plt.bar(range(len(array)), array, color='#A0A0FF')
    if (a != -1) and (b != -1):
        mark = np.zeros(LISTNUM)
        mark[a], mark[b] = array[a], array[b]
        plt.bar(range(len(mark)), mark, color='#FFA0A0')
    elif (a != -1):
        mark = np.zeros(LISTNUM)
        mark[a] = array[a]
        plt.bar(range(len(mark)), mark, color='#FFA0A0')
    plt.xlim([-1,len(array)])
    plt.text(0.01, 0.99, m, fontsize=10, horizontalalignment='left', verticalalignment='top', family='monospace', transform=ax.transAxes)
    plt.tick_params(labelbottom="off",bottom="off")
    plt.tick_params(labelleft="off",left="off")
    plt.savefig('./pic/image_{:0>6}.png'.format(count))
    #plt.show()
    plt.close('all')
    count += 1

def make_endimage(array, count, m):
    for i in range(25):
        make_image(array, count, m, -1, -1)
        count += 1

def print_progress(now, total, par):
    if (10 * (now / total)) > par:
        #sys.stdout.write("#")
        par += 1

def mix_data(array):
    for i in range(MIXNUM):
        a = random.randrange(len(array))
        b = random.randrange(len(array))
        array[a], array[b] = array[b], array[a]
    print("complete mix array")
        
def insertion_sort(array):
    print("insertion sort")
    method = "insertion sort"
    count = 0
    par = 0
    n = len(array)
    for i in range(1,n):
        tmp = array[i]
        if tmp < array[i-1]:
            j = i
            while True:
                array[j] = array[j-1]
                make_image(array, count, method, j, -1)
                count += 1
                j -= 1
                if j <= 0 or tmp >= array[j-1]:
                    break
            array[j] = tmp
        #print_progress(i, n, par)
        #sys.exit()
    make_endimage(array, count, method)

def bubble_sort(array):
    print("bubble sort")
    method = "bubble sort"
    count = 0
    par = 0
    n = len(array)
    for i in range(0, n):
        rev = range(i, n)
        for j in reversed(rev):
            if array[j-1] > array[j]:
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp
            make_image(array, count, method, j-1, -1)
            count += 1
    make_endimage(array, count, method)

def selection_sort(array):
    print("selection sort")
    method = "selection sort"
    count = 0
    par = 0
    n = len(array)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if array[j] < array[least]:
                least = j
            make_image(array, count, method, j, least)
            count += 1
        tmp = array[i]
        array[i] = array[least]
        array[least] = tmp
    make_endimage(array, count, method)

if __name__ == '__main__':
    start = time.time()

    data = array.array('i', range(1, LISTNUM))
    mix_data(data)

    #insertion_sort(data)
    #bubble_sort(data)
    selection_sort(data)

    print(time.time() - start)
