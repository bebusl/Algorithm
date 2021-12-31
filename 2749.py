n = int(input())

n = n % 1500000  # 10^K -> 15 * 10^(K-1)

arr = []
arr.append(0)
arr.append(1)

for i in range(2, n + 1):
    arr.append((arr[i - 1] + arr[i - 2]) % 1000000)

print(arr[n])
