# Sort Visualization

import array
import random
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation

LISTNUM = 100
MIXNUM  = 200

fig = plt.figure()
ims = []

# fixed seed value
random.seed(0)

def mix_data(array):
    for i in range(MIXNUM):
        a = random.randrange(LISTNUM)
        b = random.randrange(LISTNUM)
        array[a], array[b] = array[b], array[a]


def plot(array):
    im = plt.bar(range(len(array)), array, width=0.9, color='C0')
    ims.append(im)

def insertion_sort(array):
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
        plot(array)
    # result
    for i in range(3):
        plot(array)

if __name__ == '__main__':
    data = array.array('i', range(1, LISTNUM))
    mix_data(data)
    insertion_sort(data)
    ani = animation.ArtistAnimation(fig, ims, interval=100)
    ani.save('sort.gif', writer='imagemagick')
