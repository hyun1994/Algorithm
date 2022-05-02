def chaining(k,v):
    idx = hash(k) % len(hash_table)

    if hash_table[idx] != 0:
        for i in hash_table[idx]:
            if i[0] == k:
                i[1] = v
                return
        return hash_table[idx].append([k,v])
    hash_table[idx] = [[k,v]]
    return

def linear_probing(k,v):
    idx = hash(k) % len(hash_table)

    for i in range(idx, len(hash_table)):
        if hash_table[i] == 0:
            hash_table[i] = [k,v]
            return

        elif hash_table[i][0] == k:
            hash_table[i][1] = v
            return