# lv.1
# =================================================
# 예산
from itertools import combinations


def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget - i >= 0:
            budget = budget - i
            answer += 1
    return answer

# =================================================
# 폰켓몬


def solution(nums):

    return len(set(nums)) if len(set(nums)) < len(nums)/2 else len(nums)/2

    # return min(len(ls)/2, len(set(ls))) min 함수 사용!


# =================================================
# 소수 만들기


def solution(nums):
    answer = 0
    check = []
    comb = list(combinations(nums, 3))

    for i in comb:
        check = sum(i)
        re = True

        for j in range(2, check//2 + 1):
            if check % j == 0:
                re = False
                break
        if re == True:
            answer += 1

    return answer
