def counting_sort(arr, cnt, result):
    m = max(arr)

    for i in range(len(arr)):
        cnt[arr[i]] += 1

    for j in range(1, m+1):
        cnt[j] = cnt[j-1] + cnt[j+1]

    for k in range(len(arr)-1, -1, -1):
        result[cnt[arr[k]]-1] = arr[k]
        cnt[arr[k]] -= 1