# 음양 더하기
from numpy import absolute


def solution(absolutes, signs):
    answer = 0
    for i, j in zip(absolutes, signs):
        if j:
            answer += i
        else:
            answer -= i
    return answer

# return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
