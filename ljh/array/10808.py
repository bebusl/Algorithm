from collections import defaultdict, Counter

a = [chr(i) for i in range(ord('a'), ord('z')+1)]
# a to z list 만드는 법
# 1. 위와 같은 방법
# 2. string 패키지에서 string.ascii_lowercase()로 구할 수 있음.
b = Counter(input())

for i in a:
    if i in b:
        print(b[i], end=' ')
    else:
        print(0, end=' ')