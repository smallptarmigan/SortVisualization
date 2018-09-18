# sort method file

import sys
import array
import genimage as gi

def insertion_sort(array):
    print("[log] run insertion sort")
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
    print("[log] run bubble sort")
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
    print("[log] run selection sort")
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
    print("[log] run merge sort")
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
    print("[log] run quick sort")
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
    print("[log] run radix sort")
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
    
def shell_sort(array):
    print("[log] run shell sort")
    method = "shell sort"
    count = 0
    inc = 4
    while inc > 0:
        for i in range(len(array)):
            j = i
            temp = array[i]
            while j >= inc and array[j-inc] > temp:
                array[j] = array[j-inc]
                j = j -inc
            array[j] = temp
            gi.make_image(array, count, method, i, -1)
            count += 1
        
        if inc//2 != 0:
            inc = inc//2
        elif inc == 1:
            inc = 0
        else:
            inc = 1
    
    gi.make_endimage(array, count, method)

###############################################################

def shaker_sort(array):
    print("[log] run shaker_sort")
    method = "shaker sort"
    count = 0

    l = 0
    r = len(array)-1
    while l < r:

        for i in range(l,r):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                shift = i
            gi.make_image(array, count, method, i, -1)
            count += 1
        r = shift

        for i in range(r, l, -1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                shift = i
            gi.make_image(array, count, method, i, -1)
            count += 1
        l = shift

    gi.make_endimage(array, count, method)

###############################################################

def heap_sort(array):
    print("[log] run heap sort")
    method = "heap sort"
    count = 0
    n = len(array) - 1

    for i in range((n//2), -1, -1):
        array, count = downheap(array, count, method, i, n)
    for i in range(n, 0, -1):
        if array[0] > array[i]:
            array[0], array[i] = array[i], array[0]
            array, count = downheap(array, count, method, 0, i-1)
    gi.make_endimage(array, count, method)

def downheap(array, count, m, root, bot) :
    l = root * 2 + 1
    r = root * 2 + 2
    
    if l <= bot and array[l] > array[root]:
        maxch = l
    else :
        maxch = root

    if r <= bot and array[r] > array[maxch]:
        maxch = r

    if maxch != root:
        array[root], array[maxch] = array[maxch], array[root]
        array, count = downheap(array, count, m, maxch, bot)

    gi.make_image(array, count, m, root, maxch)
    count += 1

    return array, count

###############################################################

def comb_sort(array):
    print("[log] run comb sort")
    method = "comb sort"
    count = 0

    h = len(array)
    f = False

    while (h > 1 or f) :
        h = (h * 10) // 13
        f = False
        for i in range(len(array)-h):
            if array[i] > array[i+h]:
                array[i], array[i+h] = array[i+h], array[i]
            gi.make_image(array, count, method, i, i+h)
            count += 1

    gi.make_endimage(array, count, method)

###############################################################

def oddeven_sort(array):
    print("[log] run oddeven sort")
    method = "oddeven sort"
    count = 0
    
    ischange = True

    while ischange :
        ischange = False
        for i in range(0, len(array)-1, 2):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                ischange = True
            gi.make_image(array, count, method, i, i+1)
            count += 1
        for i in range(1, len(array)-1, 2):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                ischange = True
            gi.make_image(array, count, method, i, i+1)
            count += 1

    gi.make_endimage(array, count, method)

###############################################################

def stooge_sort(array):
    print("[log] run stooge sort")
    method = "stooge sort"
    count = 0
    sys.setrecursionlimit(10000)    
    array, count = stooge(array, count, method, 0, len(array)-1)
    gi.make_endimage(array, count, method)

def stooge(array, count, m, l, r):
    if array[l] > array[r]:
        array[l], array[r] = array[r], array[l]

    t = (r - l + 1) // 3

    if t < 1:
        return array, count

    array, count = stooge(array, count, m, l, r-t)
    array, count = stooge(array, count, m, l+t, r)
    array, count = stooge(array, count, m, l, r-t)

    gi.make_image(array, count, m, l, r)
    count += 1

    return array, count

###############################################################

def gnome_sort(array):
    print("[log] run gnome sort")
    method ="gnome sort"
    count = 0
    
    


    gi.make_endimage(array, count, method)
    

