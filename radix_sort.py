def radix_sort(arr):
    m = max(arr)
    d = 1
    while m/d > 1:
        counting_sort(arr, d)
        d *= 10

def counting_sort(arr, d):
    n = len(arr)
    result = [0]*(n)
    cnt = [0] * (10)

    for i in range(n):
        idx = arr[i] // d
        cnt[idx%10] += 1
    
    for j in range(1, 10):
        cnt[j] = cnt[j-1] + cnt[j]

    k = n-1
    while k >= 10:
        idx = arr[k] // d
        result[cnt[idx%10]-1] = arr[k]
        cnt[idx%10] -= 1
        k -= 1
    k = 0
    for k in range(len(arr)):
        arr[k] = result[k]