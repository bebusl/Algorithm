from collections import Counter
n = int(input())
for i in range(n):
    a, b = map(Counter, input().split())
    if a == b:
        print("Possible")
    else:
        print("Impossible")
