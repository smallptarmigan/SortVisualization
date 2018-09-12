# sort method file

import sys
import array
import genimage as gi

def insertion_sort(array):
    print("insertion sort")
    method = "insertion sort"
    count = 0
    n = len(array)
    for i in range(1,n):
        tmp = array[i]
        if tmp < array[i-1]:
            j = i
            while True:
                array[j] = array[j-1]
                gi.make_image(array, count, method, j, -1)
                count += 1
                j -= 1
                if j <= 0 or tmp >= array[j-1]:
                    break
            array[j] = tmp
        #sys.exit()
    gi.make_endimage(array, count, method)

###############################################################

def bubble_sort(array):
    print("bubble sort")
    method = "bubble sort"
    count = 0
    n = len(array)
    for i in range(0, n):
        rev = range(i, n)
        for j in reversed(rev):
            if array[j-1] > array[j]:
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp
            gi.make_image(array, count, method, j-1, -1)
            count += 1
    gi.make_endimage(array, count, method)

###############################################################

def selection_sort(array):
    print("selection sort")
    method = "selection sort"
    count = 0
    n = len(array)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if array[j] < array[least]:
                least = j
            gi.make_image(array, count, method, j, least)
            count += 1
            #sys.exit()
        tmp = array[i]
        array[i] = array[least]
        array[least] = tmp
    gi.make_endimage(array, count, method)

###############################################################

def merge_sort(array):
    print("merge sort")
    method = "merge sort"
    count = 0
    sys.setrecursionlimit(10000)
    array, count = merge(array, 0, len(array)-1, count, method)
    gi.make_endimage(array, count, method)

def merge(array, l, r, count, m):
    if r - l < 1:
        return array, count
    mid = (l + r) // 2

    merged = array[:]

    array, count = merge(array, l, mid, count, m)
    array, count = merge(array, mid+1, r, count, m)

    i = l
    j = mid + 1

    while l <= mid and j <= r:
        if(array[l] <= array[j]):
            merged[i] = array[l]
            l += 1
        else:
            merged[i] = array[j]
            j += 1
        i += 1
    
    while l <= mid:
        merged[i] = array[l]
        i += 1
        l += 1

    while j <= r:
        merged[i] = array[j]
        i += 1
        j += 1

    gi.make_image(array, count, m, -1, -1)
    count += 1

    return merged[:], count


