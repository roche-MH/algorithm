class Solution:
    def reformatNumber(self, number: str) -> str:
        import re
        number= re.sub('[ -]','',number)
        answer = []
        i,length =0,len(number)
        while i < length:
            if i+4 == length:
                answer.append(number[i:i+2])
                i+=2
            elif i+3 <= length:
                answer.append(number[i:i+3])
                i+=3
            else:
                answer.append(number[i:i+2])
                i+=2
        if len(answer)>1:
            return '-'.join(answer)
        return answer[0]
