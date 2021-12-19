def solution(lottos, win_nums):
    value = 0
    answer = [0,0]
    score = [6,6,5,4,3,2,1]
    for lotto in lottos:
        if lotto in win_nums:
            value+=1

    ez = lottos.count(0)
    
    answer[0],answer[1] = score[value+ez], score[value]
    return answer
