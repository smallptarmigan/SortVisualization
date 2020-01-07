# -*- coding: utf-8 -*-
# make image python file

import os
import array
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

OUTPUTDIR = './pic/'

def make_image(array, count, m, a, b):
    fig, ax = plt.subplots(1,1)
    plt.bar(range(len(array)), array, color='#A0A0FF')
    if (a != -1) and (b != -1):
        mark = np.zeros(len(array))
        mark[a], mark[b] = array[a], array[b]
        plt.bar(range(len(mark)), mark, color='#FFA0A0')
    elif (a != -1):
        mark = np.zeros(len(array))
        mark[a] = array[a]
        plt.bar(range(len(mark)), mark, color='#FFA0A0')
    plt.xlim([-1,len(array)])
    plt.ylim([0,len(array)+4])
    plt.text(0.01, 0.99, m, fontsize=10, horizontalalignment='left', \
             verticalalignment='top', family='monospace', transform=ax.transAxes)
    plt.tick_params(labelbottom="off",bottom="off")
    plt.tick_params(labelleft="off",left="off")
    if not os.path.exists(OUTPUTDIR):
        os.mkdir(OUTPUTDIR)
    plt.savefig(OUTPUTDIR+'image_{:0>6}.png'.format(count))
    #plt.show()
    plt.close('all')
    count += 1

def make_endimage(array, count, m):
    for i in range(len(array)):
        make_image(array, count, m, i, -1)
        count += 1
    for i in range(25):
        make_image(array, count, m, -1, -1)
        count += 1

