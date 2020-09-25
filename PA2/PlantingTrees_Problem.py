import math

def main():

    A = []
    seedlings = int(input())
    arr = input().split(' ')
    for val in arr:
        A.append(int(val))

    A = mySort(A)
    days = plant(A, seedlings)

    print(days)

    return


# The function mySort is an implementation of Mergesort, as outlined in
# "Algorithms" by Jeff Erickson in his chapter on recursion (2019, pg. 26).
# I refined the if-check in the merge function based on pseudocode outlined
# in the Top-Down Implementation of Mergesort on Wikipedia.
#
# Mergesort Complexity: The complexity of my implementation of Mergesort is O(nlogn)
#   in the average and worst cases.
#
def mySort(arr):
    n = len(arr)

    if n > 1:
        m = int(n / 2)
        sort1 = mySort(arr[0:m])
        sort2 = mySort(arr[m:n])
        arr = merge(sort1 + sort2, m)

    return arr


def merge(arr, m):
    i = 0
    j = m
    n = len(arr)
    B = [None] * n

    for k in range(0, n):
        if i < m and (j >= n or arr[i] <= arr[j]):
            B[k] = arr[i]
            i += 1
        else:
            B[k] = arr[j]
            j += 1

    return B


def plant(arr, seedlings):

    current_day = 0
    max_day = 0

    for i in range(seedlings - 1, -1, -1):
        tree_time = int(arr[i]) + 2
        max_day = max(max_day, current_day + tree_time)
        current_day += 1

    return max_day


if __name__ == '__main__':
    main()
