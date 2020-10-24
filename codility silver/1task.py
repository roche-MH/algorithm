#https://app.codility.com/cert/view/cert3AU8A9-F8KBVBKM4X4UDQKQ/
from collections import Counter
def solution(A,B):
    box = Counter(A+B).most_common(1)[0][0]
    cnt =0
    for i,v in zip(A,B):
        if i == box or v == box:
            cnt+=1
    return cnt

print(solution([2, 10, 4, 1, 4], [4, 1, 2, 2, 5]))
