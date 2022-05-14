# 체육복
def solution(n, lost, reserve):

    # 겹치는 것 제외
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

# 왼쪽부터 탐색
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)


# test
print(solution(10, [1, 2, 3, 4, 5, 6, 7, 8], [6, 7, 8, 9, 10]))
