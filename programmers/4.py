# 모의고사

def solution(answers):
    answer = []
    correct = [0, 0, 0]
    count1 = count2 = count3 = 0

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            count1 += 1
        if answers[i] == two[i % len(two)]:
            count2 += 1
        if answers[i] == three[i % len(three)]:
            count3 += 1
    correct = [count1, count2, count3]
    # print(correct)
    Max = max(correct)

    for i in range(3):
        if Max == correct[i]:
            answer.append(i+1)

    return answer


# # 런타임 에러
# def solution(answers):
#     answer = []
#     correct = [0, 0, 0]
#     count = 0

#     one = [1, 2, 3, 4, 5]
#     two = [2, 1, 2, 3, 2, 4, 2, 5]
#     three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

#     for i in range(len(answers)):
#         if one[i] == answers[i]:
#             count += 1

#     correct[0] = count
#     count = 0

#     for i in range(len(answers)):
#         if two[i] == answers[i]:
#             count += 1

#     correct[1] = count
#     count = 0

#     for i in range(len(answers)):
#         if three[i] == answers[i]:
#             count += 1

#     correct[2] = count
#     print(correct)

#     Max = max(correct)

#     for i in range(3):
#         if Max is correct[i]:
#             answer.append(i+1)

#     return answer
