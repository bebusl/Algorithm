def remove_same_value(n, d):
    while( n>1):
        if(n%d != 0):
            break
        n //= d
    return n

def solution(n):
    answer = []
    if (n % 2 == 0):
        answer.append(2)
        n = remove_same_value(n,2)

    for i in range(3, n + 1, 2):
        if (n % i == 0):
            answer.append(i)
            n = remove_same_value(n,i)

    return answer

