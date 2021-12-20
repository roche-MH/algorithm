from itertools import combibations
from collections import Counter
def solution(orders, course):
  answer = []
  for k in course:
    candidates = []
    for order in orders:
      for j in combinations(order,k):
        res = ''.join(sorted(j))
         candidates.append(res)
    sorted_candidates = Counter(candidates).most_common()
    answer += [menu for menu,cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    
    return sorted(answer)
