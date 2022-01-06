N = int(input())
arr = list(map(int, input().split()))
counts = {}

for num in arr:
    if num not in counts:
        counts[num] = 1
    else:
        counts[num] += 1

M = int(input())
input_arr = list(map(int, input().split()))
for num in input_arr:
    if num not in counts:
        print("0", end=' ')
    else:
        print(counts[num], end=' ')
print()
