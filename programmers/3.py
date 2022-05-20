from collections import defaultdict
# 신고 결과 받기


def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report = set(report)
    user_report = defaultdict(set)
    num_report = defaultdict(int)
    limited_user = []

    for i in report:
        a, b = i.split()

        num_report[b] += 1
        user_report[a].add(b)

        if num_report[b] == k:
            limited_user.append(b)

    for s in limited_user:
        for i in range(len(id_list)):
            if s in user_report[id_list[i]]:
                answer[i] += 1

    return answer


id = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]

print(solution(id, report, 2))


# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer
