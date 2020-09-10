def solution(n):
    answer=[]
    arr = [[ 0 for i in range(n)] for i in range(n)]
    di=1
    i,j = n-1,n-1
    num=1
    cnt=0

    while True:
        arr[i][j] = num
        #print(arr,di,i,j)
        num+=1
        cnt+=1

        if cnt==n:
            if n==1: break
            if di==3: di =1
            else: di+=1
            n-=1
            cnt=0
        if j<0:
            di=3
        if di == 1: # 우측 하단으로 대각이동
            i-=1
            j-=1
        elif di==2: # 좌측으로 이동
            j+=1

        elif di==3: # 상단으로 이동

            i+=1
    for i in range(len(arr)-1,-1,-1):
        for j in arr[i]:
            if j==0:
                continue
            else:
                answer.append(j)


    return answer
