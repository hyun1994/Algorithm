def merge_sort(arr, idx_s, idx_l):
    if idx_s >= idx_l:
        return
    q = (idx_s + idx_l) // 2
    merge_sort(arr, idx_s, q)
    merge_sort(arr, q+1, idx_l)
    merge(arr, idx_s, q+1, idx_l)

def merge(arr, idx_start, idx_q, idx_last):
    merged_arr = []
    s, q = idx_start, idx_q
    while s < idx_q and q <= idx_last:
        if arr[s] <= arr[q]:
            merged_arr.append(arr[s])
            s += 1
        else:
            merged_arr.append(arr[q])
            q += 1
    while s < idx_q:
        merged_arr.append(arr[s])
        s += 1
    while q <= idx_last:
        merged_arr.append(arr[q])
        q += 1
    
    s = idx_start
    for i in merged_arr:
        arr[s] = i
        s += 1