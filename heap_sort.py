def heap_sort(arr):
    # build heap
    n = len(arr)
    # arr.len//2 down to 1으로 역순으로 올라가야함
    for i in range(n//2-1, -1, -1):
        heapify(arr, i, n)

    for j in range(n-1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, 0, j)
    return arr

def heapify(arr, idx, heap_size):
    largest = idx
    left_idx = 2*idx
    right_idx = 2*idx+1

    if left_idx < heap_size and arr[left_idx] > arr[largest]:
        largest = left_idx
    if right_idx < heap_size and arr[right_idx] > arr[largest]:
        largest = right_idx
    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heapify(arr, largest, heap_size)