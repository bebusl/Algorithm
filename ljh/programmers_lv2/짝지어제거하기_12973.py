def solution(s):
    prev = []

    for i in s:
        if(len(prev) >= 1 and i == prev[-1]):
            prev.pop()
        else: prev.append(i)
    if(not len(prev)): return 1
    return 0


solution('baabaa')

# stack을 이용하는 전형적인 문제
# 괄호 치기, 짝짓기 이런건 다 스택으로 해결~