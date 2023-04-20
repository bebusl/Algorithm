def solution(N, number):
    memo = {1:set(), 2:set(), 3:set(),4:set(),5:set(),6:set(),7:set(),8:set()}
    for k in range(1,9):
        for i in range(1,k//2+1):
            j = k-i
            for t in memo[i]:
                for p in memo[j]:
                    temp = set()
                    temp.add(t+p)
                    temp.add(t*p)
                    temp.add(t-p)
                    if(p!=0): temp.add(t/p)
                    if(t!=0): temp.add(p/t)
                    temp.add(p-t)
                    if(number in temp):
                        return k
                    memo[k].update(temp)

            ## 여기서 number가 만들어진다면, return N
        str_N = str(N)
        successive = int(str_N*k)
        if(successive == number or -successive == number):
            return k
        memo[k].add(successive)
        memo[k].add(-successive)
        print(memo)
    return -1

res = solution(5,12)
print(res)