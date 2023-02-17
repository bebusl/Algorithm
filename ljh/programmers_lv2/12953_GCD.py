from functools import reduce
from collections import defaultdict

# def factorization(arr):
#     result = defaultdict(int)
#     for num in arr:
#         re = defaultdict(int)
#         copy_num = num
#         factor = 2
#         is_prime = True
#         while(factor<num**0.5+1):
#             if(copy_num%factor ==0):
#                 re[factor]+=1
#                 copy_num//=factor
#                 is_prime=False
#             else:
#                 factor +=1
#         if(copy_num>1):
#             re[copy_num]+=1
#
#
#         for key,value in re.items():
#             if(result[key]>=value):
#                 continue
#             else :
#                 result[key]=value
#     multiple = 1
#     for key,value in result.items():
#         multiple*=(key**value)
#     return multiple
# 이건 처음 풀이.
# GCD사용하지 않고 직접 소인수분해해서 공통된 부분은 그래도 두고 계속 dict를 업데이트하는 식으로 수정

def GCD(a,b):
    if(b>a):
        a,b = b,a
    if(a%b==0):
        return b
    else:
        return GCD(b, a%b)


def solution(arr):
    prev = arr[0]
    for idx in range(1,len(arr)):
        gcd = GCD(prev,arr[idx])
        print("GDC",gcd)
        prev = (prev*arr[idx] )//gcd
    return prev


print(solution([12, 32, 45, 67, 72]))
print("IS 96480")



## 여러 수의 최소 공약수를 구하라
## array를 돌면서