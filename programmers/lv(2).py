# 직사각형 별찍기
a, b = map(int, input().strip().split(' '))
str = "*"*a
for i in range(b):
    print(str)

a, b = map(int, input().strip().split(' '))
answer = ('*'*a + '\n')*b
print(answer)

# 행렬의 덧셈


def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1


def sumMatrix(A, B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    return answer


# 짝수와 홀수
lambda num: "Even" if num % 2 == 0 else "Odd"


def solution(num):
    return "Even" if num % 2 == 0 else "Odd"

# 자릿수 더하기
# sum함수 사용


def solution(n):
    return sum(int(i) for i in str(n))

# for문 사용


def solution(n):
    answer = 0
    for i in (str(n)):
        answer += int(i)

    return answer

# 핸드폰 번호 가리기


def solution(phone_number):
    return phone_number.replace(phone_number[0:len(phone_number)-4], "*"*(len(phone_number)-4))


def solution(phone_number):
    return "*"*(len(phone_number)-4) + phone_number[-4:]

# 평균 구하기


def solution(arr):
    return sum(arr)/len(arr)

    # 예외처리
    # if len(arr)==0 : return 0

# 제일 작은 수 제거하기


def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr

# x만큼 간격이 있는 n개의 숫자


def solution(x, n):
    return [i*x for i in range(1, n+1)]

# 자연수 뒤집어 배열로 만들기


def solution(n):
    answer = [int(i) for i in str(n)]
    answer.reverse()
    return answer


def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]


def digit_reverse(n):
    return list(map(int, reversed(str(n))))

# 콜라츠 추측


def solution(num):
    count = 0
    if num == 1:
        return count
    while(count != 500):
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        count += 1
        if num == 1:
            return count

    return -1
