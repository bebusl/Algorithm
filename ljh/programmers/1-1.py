

def solution(n):
    answer = 0
    arr = set();
    if n == 0:
        return 0
    if n==1:
        return 1
    for i in range(1,n//2):
        if(n%i==0):
            arr.add(i)
            arr.add(n//i)
    answer = sum(arr)
    return answer

print("RESULT ::" ,solution(1))