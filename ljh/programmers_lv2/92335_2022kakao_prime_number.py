def translate(n, number):
    n_ory = ''
    while (number > 0):
        n_ory += '%d' % (number % n)
        number //= n
    return n_ory[::-1]


def primeArray(max_value):
    uclid = [False, False]
    uclid.extend([True for i in range(max_value-1)])
    idx = 2
    while (True):
        if (not uclid[idx]):
            idx += 1
            continue
        if (idx > max_value**0.5):
            break
        tmp_idx = 2
        while (True):
            if (idx * tmp_idx > max_value):
                break
            uclid[idx * tmp_idx] = False
            tmp_idx+=1
        idx += 1
    return uclid


def solution(n, k):
    answer = 0
    n_ory = translate(k,n)
    number_set = list(map(int,filter(None,n_ory.split('0'))))

    max_num =max(number_set)
    uclid = primeArray(max_num)

    for num in number_set:
        if(uclid[num]):
            answer+=1

    return answer if answer else -1

print(solution(110011,10))