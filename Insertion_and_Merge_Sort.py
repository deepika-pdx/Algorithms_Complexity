import math
import time

import numpy as np
from xlwt import Workbook

# Workbook is created
wb = Workbook()
output_excel = wb.add_sheet('Sheet 1')


def generateRandomArray(n):
    if n > 0:
        random_array = np.random.randint(100, size=(n))
        return random_array
    return


def generateSortedArray(n):
    if n > 0:
        sorted_array = np.random.randint(100, size=(n))
        sorted_array.sort()
        return sorted_array
    return


def insertionSort(A):
    n = len(A)
    for j in (number + 1 for number in range(n - 1)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


def merge(B, C):
    i = 0
    j = 0
    N = []
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            N.append(B[i])
            i = i + 1
        else:
            N.append(C[j])
            j = j + 1
    if i == len(B):
        N.extend(C[j:])
    else:
        N.extend(B[i:])
    return N


def mergeSort(A):
    n = len(A)
    if n == 1:
        return A
    mid = math.floor(n / 2)
    B = mergeSort(A[0:mid])
    C = mergeSort(A[mid:n])
    return merge(B, C)


# Comparing running time of random and sorted arrays
# random_sizes = np.random.randint(500, 3400, 15)
# random_sizes.sort()
# count = 0
# sorted_arrays = []
# for size in random_sizes:
#     A = generateRandomArray(size)
#     B = A.copy()
#
#     # -----------------Insertion Sort on random arrays--------------------------------
#     start_time = time.time()
#     sorted_array = insertionSort(A)
#     sorted_arrays.append(sorted_array)
#     insertion_sort_time_taken = (time.time() - start_time)
#     output_excel.write(count, 0, str(size))
#     output_excel.write(count, 1, insertion_sort_time_taken)
#
#     # -----------------Merge Sort on random arrays--------------------------------
#     start_time = time.time()
#     mergeSort(B)
#     merge_sort_time_taken = (time.time() - start_time)
#     output_excel.write(count, 3, str(size))
#     output_excel.write(count, 4, merge_sort_time_taken)
#     count = count + 1
# wb.save('xlwt example.xls')

# random_sizes = [4200, 4201, 4202, 4203, 4204, 4205, 4206, 4207, 4208, 4209, 4210, 4211, 4212, 4213, 4214]
# count = 0
# for size in random_sizes:
#     A = generateRandomArray(size)
#     A.sort()
#     B = A.copy()
#
#     # -----------------Insertion Sort on sorted arrays--------------------------------
#     start_time1 = time.time()
#     insertionSort(A)
#     insertion_sort_time_taken = (time.time() - start_time1)
#     output_excel.write(count, 0, str(len(A)))
#     output_excel.write(count, 1, insertion_sort_time_taken)
#
#     # -----------------Merge Sort on sorted arrays--------------------------------
#     start_time2 = time.time()
#     mergeSort(B)
#     merge_sort_time_taken = (time.time() - start_time2)
#     output_excel.write(count, 3, str(len(B)))
#     output_excel.write(count, 4, merge_sort_time_taken)
#     count = count + 1
# wb.save('xlwt example.xls')


# Determining number of elements that are out of order
in_order_count = 1000
out_of_order_count = 0
count = 0
while in_order_count != 0:
    A = generateSortedArray(in_order_count)
    R = generateRandomArray(out_of_order_count)
    if R is not None:
        A = np.append(A, R)
    B = A.copy()

    # -----------------Insertion Sort out of order--------------------------------
    start_time = time.time()
    insertionSort(A)
    insertion_sort_time_taken = (time.time() - start_time)
    output_excel.write(count, 0, str(out_of_order_count))
    output_excel.write(count, 1, insertion_sort_time_taken)

    # -----------------Merge Sort out of order--------------------------------
    start_time = time.time()
    mergeSort(B)
    merge_sort_time_taken = (time.time() - start_time)
    output_excel.write(count, 3, str(out_of_order_count))
    output_excel.write(count, 4, merge_sort_time_taken)
    count = count + 1
    in_order_count = in_order_count - 50
    out_of_order_count = out_of_order_count + 50
wb.save('xlwt example.xls')
