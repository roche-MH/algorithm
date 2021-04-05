def reversort(array):
    cnt = 0
    change = False
    for i in range(len(array)-1):
        tmp = array[i]
        for idx in range(i, len(array)):
            if array[idx] < tmp:
                change = True
                j = idx
                tmp = array[idx]
        if change:
            array[i:j+1] = array[i:j+1][::-1]
            cnt += j-i + 1
        else:
            cnt += 1
        change = False
    return cnt
case_=int(input())
case =1
for _ in range(case_):
    n = int(input())
    array = list(map(int,input().split(' ')))
    print(f"Case #{case}: {reversort(array)}")
    case+=1
