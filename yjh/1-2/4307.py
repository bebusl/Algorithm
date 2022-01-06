from sys import stdin, stdout

input = stdin.readline

T = int(input())

for t in range(T):
    l, n = map(int, input().split())
    answer_min, answer_max = 0, 0
    for i in range(n):
        v = int(input())
        diff = abs(l - v)
        if v < diff:
            min_, max_ = v, diff
        else:
            min_, max_ = diff, v
        if min_ > answer_min:
            answer_min = min_
        if max_ > answer_max:
            answer_max = max_

    stdout.write(f'{answer_min} {answer_max}\n')

