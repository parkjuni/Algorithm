# K번째 수
def solution(array, commands):
    answer = []

    for i, j, k in commands:

        slicing = array
        slicing = slicing[i-1: j]

        slicing.sort()
        answer.append(slicing[k-1])

    return answer

    # def solution(array, commands):
    #     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
