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
    merged = array[:]

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
        gi.make_image(merged, count, m, i-1, -1)
        count += 1
    
    while l <= mid:
        merged[i] = array[l]
        i += 1
        l += 1
        gi.make_image(merged, count, m, i-1, -1)
        count += 1

    while j <= r:
        merged[i] = array[j]
        i += 1
        j += 1
        gi.make_image(merged, count, m, i-1, -1)
        count += 1

    return merged[:], count

###############################################################

def quick_sort(array):
    print("quick sort")
    method = "quick sort"
    count = 0
    sys.setrecursionlimit(10000)
    array, count = quick(array, 0, len(array)-1, count, method)
    gi.make_endimage(array, count, method)

def quick(array, l, r, count, m):
    p = array[l]
    lh = l
    rh = r

    while l < r:
        while array[r] >= p and l < r:
            r -= 1
        
        if l != r:
            array[l] = array[r]
            l += 1

        gi.make_image(array, count, m, l, r)
        count += 1
        
        while array[l] <= p and l < r:
            l += 1

        if l != r:
            array[r] = array[l]
            r -= 1
    
        gi.make_image(array, count, m, l, r)
        count += 1

    array[l] = p
    p = l
    l = lh
    r = rh
    if l < p:
        array, count = quick(array, l, p-1, count, m)
    if r > p:
        array, count = quick(array, p+1, r, count, m)

    return array, count

###############################################################

def radix_sort(array):
    print("radix sort")
    method = "radix sort"
    count = 0
    r = 10
    m = 1

    rad = array[:]
    y = array[:]

    while m <= r:
        for i in range(len(array)):
            rad[i] = (array[i] // m) % 10
        k = 0
        for i in range(10):
            for j in range(len(array)):
                if rad[j] == i:
                    y[k] = array[j]
                    k += 1
        for i in range(len(array)):
            array[i] = y[i]
            gi.make_image(array, count, method, i, -1)
            count += 1
        m *= 10

    gi.make_endimage(array, count, method)

###############################################################
    


