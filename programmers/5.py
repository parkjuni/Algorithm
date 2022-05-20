# 완주하지 못한 선수

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            break
        else:
            i += 1
    answer = participant[i]

    return answer

    # def solution(participant, completion):
    # participant.sort()
    # completion.sort()
    # for i in range(len(completion)):
    #     if participant[i] != completion[i]:
    #         return participant[i]
    # return participant[len(participant)-1]
