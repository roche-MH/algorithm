def findCost(arr):
    res = 0
    for i in range(len(arr) - 1):
        j = arr.index(min(arr[i:]))
        arr[i:j + 1] = arr[i:j + 1][::-1]
        res += j - i + 1
    return res

def findCombos(indices, curr):
    if not indices:
        return [curr]
    res = []
    for i in indices:
        newIndices = indices[:]
        newIndices.remove(i)
        res.extend(findCombos(newIndices, curr + [i]))
    return res


for case in range(1, int(input()) + 1):
    size, cost = [int(x) for x in input().split()]
    combos = findCombos([i for i in range(1, size + 1)], [])


    ans = "IMPOSSIBLE"
    for array in combos:
       
        if findCost(array[:]) == cost:
            ans = " ".join([str(x) for x in array])

    print(f"Case #{case}: {ans}")
