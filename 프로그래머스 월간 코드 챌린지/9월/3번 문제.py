def solution(a):
    if len(a) == 1:
        answer=1
    answer=2
    bool_T = [False] * len(a)
    L_min_num = a[0]
    for i in range(1,len(a)-1):
        if a[i] < L_min_num:
            L_min_num = a[i]
            answer+=1
            bool_T[i]=True

    R_min_num = a[-1]
    for i in range(len(a)-1,-1,-1):
        if a[i] < R_min_num:
            R_min_num = a[i]
            if bool_T[i]: continue
            answer+=1
            bool_T[i]=True

    return answer
