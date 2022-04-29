import random
def quick_sort(arr, idx_start, idx_last):
    if idx_start >= idx_last:
        return
    if idx_start < idx_last:
        q = random_partition(arr, idx_start, idx_last)
        quick_sort(arr, idx_start, q-1)
        quick_sort(arr, q+1, idx_last)

def partition(arr, idx_start, idx_last):
    pivot = arr[idx_last]
    i = idx_start - 1
    for j in range(idx_start, idx_last):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[idx_last] = arr[idx_last], arr[i+1]
    return i+1

def random_partition(arr, idx_start, idx_last):
    i = random.randrange(idx_start, idx_last+1)
    arr[i], arr[idx_last] = arr[idx_last], arr[i]
    return partition(arr, idx_start, idx_last)