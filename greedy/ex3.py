# 0321 이해 못함;;.. 어렵다
n, k = map(int, input().split())

result = 0
while 1:
    target = (n//k)*k
    result += (n-target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)
