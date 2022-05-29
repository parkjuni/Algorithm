# 서울에서 김서방 찾기
def solution(seoul):
    s = "김서방은 {0}에 있다".format(seoul.index("Kim"))
    return s


def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

# 문자열을 정수로 바꾸기


def solution(s):

    return int(s)


def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result

# 문자열 다루기 기본


def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()


def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

# 두 정수 사이의 합


def solution(a, b):
    x = max(a, b)
    y = min(a, b)

    if (x-y-1) % 2 == 0:
        return (x+y)*((x-y-1)//2+1)
    else:
        return (x+y)*((x-y-1)//2+1) + (x+y)/2


def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

# 가운데 글자 가져오기


def solution(s):
    if len(s) % 2 == 1:
        s = s[int(len(s)/2)]
    else:
        s = s[int(len(s)/2)-1] + s[int(len(s)/2)]

    return s


def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]

# 수박수박수박수~?


def solution(n):
    s = ""
    for i in range(n):
        s += "수" if i % 2 == 0 else "박"
    return s


def water_melon(n):
    s = "수박" * n
    return s[:n]

# 문자열 내림차순 배치하기


def solution(s):
    return "".join(sorted(s, reverse=True))

# 문자열 내 p와 y의 개수


def solution(s):
    p = y = 0
    s = s.lower()
    for i in s:
        if i == 'p':
            p += 1
        if i == 'y':
            y += 1
    return p == y


def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

# 나누어 떨어지는 숫자 배열


def solution(arr, divisor):
    answer = [-1]
    check = 0
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            check += 1
    if check != 0:
        answer.remove(-1)

    answer.sort()
    return answer


def solution(arr, divisor): return sorted(
    [n for n in arr if n % divisor == 0]) or [-1]


def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]
