"""
애너그램 관계에 있도록 삭제해야 하는 문자의 최소수
1. string a와 string b에서
"""

from collections import Counter

a = Counter(input())
b = Counter(input())

a_keys = set(a.keys())
b_keys = set(b.keys())

cnt = 0

for a_key in a:


for a_key in a_keys:
    if a_key in b_keys:
        cnt += a[a_key] - b[a_key] if a[a_key] > b[a_key] else b[a_key] - a[a_key]
        b_keys.remove(a_key)
    else:
        cnt += a[a_key]

for b_key in b_keys:
    cnt += b[b_key]

print(cnt)
# 그냥 둘이 다르면 무조건적으로 cnt에 반영하면 되는것임,,! 흐흐..

# 문자열, 브론즈2 애너그램 만들기
# 더 좋은 해결책. Counter의 method를 잘 활용하면 이케 쉽게 풀 수 있음.
# from collections import Counter
# a = Counter(input())
# b = Counter(input())
# print(sum((a-b).values()) + sum((b-a).values()))


# f, s = [0 for _ in range(26)], [0 for _ in range(26)]
# first, second = input(), input()
# for i in range(len(first)):
#     f[ord(first[i]) - 97] += 1
# for i in range(len(second)):
#     s[ord(second[i]) - 97] += 1
# print(sum([abs(f[i]-s[i]) for i in range(26) if f[i] != s[i]]))

# Counter method 정리 : https://dongdongfather.tistory.com/m/70