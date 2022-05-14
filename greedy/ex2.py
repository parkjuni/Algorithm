from unittest import result


n, m = map(int, input().split())

result = 0

# 1
# for _ in range(n):
#     data = list(map(int, input().split()))
#     min_result = min(data)
#     result = max(result, min_result)

# 2
for _ in range(n):
    data = list(map(int, input().split()))
    min_result = 10001
    for a in data:
        min_result = min(min_result, a)

    result = max(result, min_result)

print(result)
