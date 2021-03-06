#Ryan Cardin
#Sumedh Saurabh
#Kyle Cline
#Discrete Math 2 Project 2
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt
import time
import threading
import sys
import gc
import math

## Functions:
# Part 1 - Kyle:

# Part 2 - Ryan:
## calculates insertion comparisons
def getCn(n):
    return (n * n) * .5 + (.5 * n ) - 1

def Insertionsort(array):
    start = time.time() ## begin clock
    for i in range(1, len(array)):##Start iteration through the array from the second element, making the sorted array a length of 1, the first element
        check = array[i]##This is the item being compared to the sorted array
        move = i - 1##this is the element in the sorted array being compared to the check element
        while move >= 0 and array[move] > check:##Find where in the sorted array the check element belongs
            array[move + 1] = array[move]##Shifting the elements up one space to make room for the check element
            move -= 1##moving our comparing element in the sorted array back one
        array[move + 1] = check##inserting the element in the position where the item behind is no longer greater than it or if there is nothing left
    end = time.time() ## end clock
    return (end-start)

# Part 3 - Sumedh:
## calculates merge comparisons
def getMn(n): ## Python has a recursion limit so will only go up to 996 iterations
    sys.setrecursionlimit(sys.getrecursionlimit() + 1)
    if n == 1:
        return  0
    return getMn(n // 2) + getMn(math.ceil(n / 2)) + int(n - 1)

## ascending sort merge function
## will merge both left and right sides of array into ascending order
def merge(arr,low,mid,high):
    ## size_left is size of left part and size_right is size
    ## of right part
    size_left = mid - low + 1
    size_right = high - mid

    left = [0]*size_left ## Left Array of 0's
    right = [0]*size_right ## Right Array of 0's
  

    i = 0 ## Array 1
    j = 0 ## Array 2
  
    ## storing values in left part
    for x in range(0,size_left):
        left[x] = arr[x + low]
  
    ## storing values in right part
    for x in range(0,size_right):
        right[x] = arr[x + mid + 1]
  
    k = low ## merged array
  
    ## merge left and right in ascending order
    while i < size_left and j < size_right:
        if left[i] <= right[j]:
            arr[k] = left[i] ## merged array takes left array element
            ##k+=1
            i+=1
        else:
            arr[k] = right[j] ## merged array takes right array element
            ##k+=1
            j+=1
        k+=1

    ## Leftovers

    ## insert remaining values from left
    while i < size_left:
        arr[k] = left[i]
        k+=1
        i+=1
  
    ## insert remaining values from right
    while j < size_right:
        arr[k] = right[j]
        k+=1
        j+=1

## threaded recursive merge sort function
## depending on size of array may create way more than 2 threads
def merge_sort(arr, low,high):
    ## calculating mid point of array
    mid = low + (high - 1) // 2
    if low < high:
        try:
            ## calling first half in a thread
            task1 = threading.Thread(target=merge_sort,args=(arr, low, mid))

            ## calling second half in a thread
            task2 = threading.Thread(target=merge_sort,args=(arr, mid + 1, high))

            ## threads
            task1.start() ## starts left merge sort
            task2.start() ## starts right merge sort

            ## merging the two halves
            merge(arr, low, mid, high)
            task1.join()
            task2.join()
        except:
            print("Thread - Break")
        finally:
            print("Merge sorting...")
    return 0

## threaded merge sort execution time calculation function
def merge_sort_time(arr):
    size = len(arr)
    start = time.time()  ## begin clock
    merge_sort(arr, 0, size-1)
    end = time.time()  ## end clock
    return end - start

#Part 1 - Kyle
#...........................Analysis 1a...........................
# Construct lines
# n >= 1 && n=1..10
n = np.linspace(1, 10, 2000)

# y >= (1/2)n
y1 = n

# y <= n - |n/2| + 1
y2 = n

# Make plot
plt.title('Analysis 1a')
plt.plot(n, y1, label=r'(1/2)n = Ω(n)')
plt.plot(n, y2, label=r'n - |n/2| + 1= Ω(n)')

plt.xlim((0, 12))
plt.ylim((0, 7))
plt.xlabel(r'$n$')
plt.ylabel(r'$y$')

# Fill feasible region
y5 = np.minimum(y2, 10)
y6 = np.maximum(y1, 0.5)
plt.fill_between(n, y5, y6, where=y5>y6, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
plt.savefig('Analysis_1a.png')
#..................................................................


#...........................Analysis 1b...........................
# Construct lines
# n >= 3 && n=1..10
n = np.linspace(3, 10, 2000)

## y >= (1/2)n
#y1 = 0*n
#
## y <= n - ⌊n/2⌋ + 1
#y2 = n - np.floor(n/2) + 1
#
## y <= n
#y3 = n

# y >= 0
y1 = 0*n

# y <= n - ⌊n/2⌋ + 1
y2 = n

# y <= n
y3 = n

# Make plot
plt.title('Analysis 1b')
plt.plot(n, y1, 'gp', label=r'y ≥ 0 = O(c)')
plt.plot(n, y2, 'r', label=r'y ≤  n - ⌊n/2⌋  + 1 = O(n)')
plt.plot(n, y3, 'b', label=r'y ≤  n = O(n)')

plt.xlim((0, 12))
plt.ylim((0, 10))
plt.xlabel(r'$n$')
plt.ylabel(r'$y$')

# Fill feasible region
y5 = np.minimum(y2, -1)
y6 = np.maximum(y1, 11)
plt.fill_between(n, y5, y6, where=y5<=y6, color='grey', alpha=0.5)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
plt.savefig('Analysis_1b.png')
#..................................................................


#...........................Analysis 1c...........................
# Construct lines
# n >= 3 && n=1..10
n = np.linspace(3, 10, 2000)

# y >= n^2
y1 = n**2

# y <= n
y2 = n

# y <= n^2
y3 = n**2

# Make plot
plt.title('Analysis 1c')
plt.plot(n, y1, 'gp', label=r'y ≥ n^2')
plt.plot(n, y2, 'r', label=r'y ≤ n')
plt.plot(n, y3, 'b', label=r'y ≤ n^2')

plt.xlim((0, 12))
plt.ylim((0, 20))
plt.xlabel(r'$n$')
plt.ylabel(r'$y$')

# Fill feasible region
y5 = np.minimum(y3, y2)
y6 = np.maximum(y2, y1)
plt.fill_between(n, y5, y6, where=y5<=y6, color='grey', alpha=0.5)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
plt.savefig('Analysis_1c.png')
#..................................................................

#...........................Analysis 1d...........................
# Construct lines
# n >= 3 && n=1..10
n = np.linspace(3, 10, 2000)

# y >= n^2
y1 = n**2

# y <= n
y2 = n

# Make plot
plt.title('Analysis 1d')
plt.plot(n, y1, 'g', label=r'y ≥ n^2')
plt.plot(n, y2, 'r', label=r'y ≤ n')

plt.xlim((0, 12))
plt.ylim((0, 20))
plt.xlabel(r'$n$')
plt.ylabel(r'$y$')

# Fill feasible region
y5 = np.minimum(0, y1)
y6 = np.maximum(y2, y2)
plt.fill_between(n, y5, y6, where=y5<=y6, color='grey', alpha=0.5)

y7 = np.minimum(y1, y1)
y8 = np.maximum(y1, 20)
plt.fill_between(n, y7, y8, where=y5<=y6, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
plt.savefig('Analysis_1d.png')
#..................................................................


#...........................Analysis 1e...........................
# Construct lines
# n >= 21 && n=1..10
n = np.linspace(2, 10, 2000)

# y >= n^3
y1 = n**3

# y <= n^2
y2 = n**2

# y <= n^3
y3 = n**3

# Make plot
plt.title('Analysis 1e')
plt.plot(n, y1, 'gp', label=r'y ≥ n^2')
plt.plot(n, y2, 'r', label=r'y ≤ n')
plt.plot(n, y3, 'b', label=r'y ≤ n^2')

plt.xlim((0, 12))
plt.ylim((0, 20))
plt.xlabel(r'$n$')
plt.ylabel(r'$y$')

# Fill feasible region
y5 = np.minimum(y1, y2)
y6 = np.maximum(y2, y3)
plt.fill_between(n, y5, y6, where=y5<=y6, color='grey', alpha=0.5)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
plt.savefig('Analysis_1e.png')
#..................................................................

#Part 2 - Ryan
#Part a --> Located Under Functions
#part c
array1 = [1]
array2 = [100-i for i in range(100)]
array3 = [200-i for i in range(200)]
array4 = [300-i for i in range(300)]
array5 = [400-i for i in range(400)]
array6 = [500-i for i in range(500)]
array7 = [600-i for i in range(600)]
array8 = [700-i for i in range(700)]
array9 = [800-i for i in range(800)]
array10 = [900-i for i in range(900)]
array11 = [996-i for i in range(1000)]

time1 = Insertionsort(array1)
time2 = Insertionsort(array2)
time3 = Insertionsort(array3)
time4 = Insertionsort(array4)
time5 = Insertionsort(array5)
time6 = Insertionsort(array6)
time7 = Insertionsort(array7)
time8 = Insertionsort(array8)
time9 = Insertionsort(array9)
time10 = Insertionsort(array10)
time11 = Insertionsort(array11)

#Part d
xvals = [1,100,200,300,400,500,600,700,800,900,1000]
yvals = [time1,time2,time3,time4,time5,time6,time7,time8,time9,time10,time11]
plt.plot(xvals, yvals)
plt.xlabel('Number of Elements')
plt.ylabel('Time of Computation')
plt.title('Part C')
plt.show()

xvals = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
yvals = [getCn(1), getCn(100), getCn(200), getCn(300), getCn(400), getCn(500), getCn(600), getCn(700), getCn(800), getCn(900), getCn(1000)]
plt.plot(xvals, yvals)
plt.title('Part D')
plt.xlabel('Number of Elements')
plt.ylabel('Number of Comparisons')
plt.show()

#Part 3 - Sumedh
## B:
arr1 = [1]
arr2 = [100-i for i in range(100)]
arr3 = [200-i for i in range(200)]
arr4 = [300-i for i in range(300)]
arr5 = [400-i for i in range(400)]
arr6 = [500-i for i in range(500)]
arr7 = [600-i for i in range(600)]
arr8 = [700-i for i in range(700)]
arr9 = [800-i for i in range(800)]
arr10 = [900-i for i in range(900)]
arr11 = [1000-i for i in range(1000)] ## Python has a recursion limit

input("\n\nMerge sort will occur recursively. Be patient.\n\nPress Enter to start the sorting process...")

time1 = merge_sort_time(arr1)
time2 = merge_sort_time(arr2)
time3 = merge_sort_time(arr3)
time4 = merge_sort_time(arr4)
time5 = merge_sort_time(arr5)
time6 = merge_sort_time(arr6)
time7 = merge_sort_time(arr7)
time8 = merge_sort_time(arr8)
time9 = merge_sort_time(arr9)
time10 = merge_sort_time(arr10)
time11 = merge_sort_time(arr11)

print("\n\nMerge Sorting has finished...\n\nPlease look at the graphs\n\n")

try:
    x_vals1 = [1,100,200,300,400,500,600,700,800,900,1000]
    y_vals1 = [time1,time2,time3,time4,time5,time6,time7,time8,time9,time10,time11]
    plt.plot(x_vals1, y_vals1)
    plt.xlabel('Number of Elements')
    plt.ylabel('Time of Computation')
    plt.title('Part C')
    plt.show()

    ## Cannot perform this step due to python having a recursion limit.
    x_vals2 = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    y_vals2 = [getMn(1), getMn(100), getMn(200), getMn(300), getMn(400), getMn(500), getMn(600), getMn(700), getMn(800), getMn(900), getMn(1000)]
    plt.plot(x_vals2, y_vals2)
    plt.title('Part D')
    plt.xlabel('Number of Elements')
    plt.ylabel('Number of Comparisons')
    plt.show()
except:
    print("Recursion Limit is low on Python,\n so there are performance issues with calculating Mn.")
finally:
  print("Done...")
  gc.collect()
  sys.exit()