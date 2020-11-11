def two(a):
    b = []
    for i in range(0,len(a)):
        if i == len(a)-1:
            b.append(a[i])
        else:
            b.append((a[i],a[i+1]))
    return b

from itertools import combinations
from collections import Counter
import itertools
def solution(a):
    for i in range(2,len(a)+1):
        answer = list(permutations(a,i))

        for idx in range(len(answer)):
            print(answer[idx])
            arr = two(answer[idx])
            print(arr)
            chain=list(itertools.chain.from_iterable(arr))
                #print(arr,chain)
                #print(Counter(chain), len(chain), arr)
            if Counter(chain).most_common(1)[0][1] == len(arr):
                    #print(arr)
                
                qwer = chain
        return len(qwer)

#print(map(lambda a,b : a
print(solution([5,2,3,3,5,3]))
