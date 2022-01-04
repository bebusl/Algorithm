N, S = map(int, input().split())

arr = list(map(int, input().split()))

interval_sum, answer, end = 0, 0, 0

for start in range(N):
    while interval_sum < S and end < N:
        interval_sum += arr[end]
        end += 1
    if interval_sum >= S:
        if answer == 0:
            answer = end - start
        else:
            answer = min(answer, end - start)

    interval_sum -= arr[start]

print(answer)