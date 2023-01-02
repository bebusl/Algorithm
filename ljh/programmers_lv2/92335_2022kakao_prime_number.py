import math
def translate(n, number):
    n_ory = ''
    while (number >= 1):
        n_ory += str(number%n)
        number //= n
    return n_ory[::-1]

def isPrime(value):
    if(value ==1 ):
        return False
    for i in range(2, math.floor(value**0.5)+1):
        if(value % i == 0):
            return False
    return True

def solution(n, k):
    answer = 0
    n_ory = translate(k,n)
    number_set = list(map(int,filter(None,n_ory.split('0'))))

    for num in number_set:
        if(isPrime(num)):
            answer+=1

    return answer