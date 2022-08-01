import sys
input = sys.stdin.readline

"""
입력받음
0~9까지 팩이 들ㅓㅆ는데
6과 9는 치환 가능
"""
checked = [0 for i in range(10)]
cnt = 0

n = input().strip('\n')
for i in n:
    checked[int(i)]+=1

checked_ = [checked[0],checked[1],checked[2],checked[3],checked[4],checked[5],checked[7],checked[8]]
sumofSixandNine = checked[6]+checked[9]
if(sumofSixandNine <= max(checked_)*2):
    print(max(checked_))
else:
    print((sumofSixandNine)//2 if (sumofSixandNine)%2 == 0 else (sumofSixandNine)//2+1)


"""
나랑 연산시간 6배차이남.. 아마 저 checked과정이 잘못된 것같음.
if연산을 하지도 않음.
perfect answer:

n = input()
lst = []
for num in '0123456789':
    lst.append(n.count(num))
lst[6] = (lst[6]+lst[9]+1)//2
del lst[9]
print(max(lst))
"""