# 숫자열과 문자열
# replace 사용
def solution(s):
    answer = 0
    eng_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    for i in eng_dict.items():
        s = s.replace(i[0], str(i[1]))

    answer = int(s)
    return answer


# test
print(solution('one23two'))
print(solution('nine24eight'))


# def solution(s):
#     words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

#     for i in range(len(words)):
#         s = s.replace(words[i], str(i))

#     return int(s)
