# lv.1
# 내적
def solution(a, b):

    return sum(a[i]*b[i] for i in range(len(a)))

# 1
# def solution(a, b):

#     return sum([x*y for x, y in zip(a,b)])

# 2
# solution = lambda x, y: sum(a*b for a, b in zip(x, y))

# ==========================================


# 없는 숫자 더하기
def solution(numbers): return sum(i for i in range(10) if i not in numbers)

# #1
# solution = lambda x: sum(range(10)) - sum(x)


# #2
# def solution(numbers):
#     return 45 - sum(numbers)

# ==========================================
# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if sum(1 for j in range(1, i+1) if i % j == 0) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer

    # def solution(left, right):
    # answer = 0
    # for i in range(left,right+1):
    #     if int(i**0.5)==i**0.5:
    #         answer -= i
    #     else:
    #         answer += i
    # return answer


# ==========================================
# 로또의 최고 순위와 최저 순위

    def solution(lottos, win_nums):
        answer = []
        record = [6, 6, 5, 4, 3, 2, 1]
        min = len(list(set(lottos) & set(win_nums)))
        answer.append(record[min + lottos.count(0)])
        answer.append(record[min])
        return answer

    # def solution(lottos, win_nums):

        # rank=[6,6,5,4,3,2,1]

        # cnt_0 = lottos.count(0)
        # ans = 0
        # for x in win_nums:
        #     if x in lottos:
        #         ans += 1
    # return rank[cnt_0 + ans],rank[ans]
