from itertools import combinations
def solution(numbers):
    answer = [sum(i) for i in combinations(numbers,2)]
    return sorted(list(set(answer)))
