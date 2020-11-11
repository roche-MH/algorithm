def solution(s):
    zero,i = 0,0
    while s != '1':
        i+=1
        zero+=s.count('0')
        s=''.join(s.split('0'))
        s = str(bin(len(s))[2:])
    return [i,zero]
print(solution(	"110010101001"))
