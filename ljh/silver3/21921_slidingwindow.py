ARRAY_LEN, WINDOW_SIZE = map(int, input().split())
ARRAY = list(map(int, input().split()))

start_point =0
max_value = -1
count = -1
tmp = sum(ARRAY[start_point:start_point+WINDOW_SIZE])
while(start_point+WINDOW_SIZE <= ARRAY_LEN):
    if(start_point - 1 >= 0):
        tmp -= ARRAY[start_point-1]
        tmp += ARRAY[start_point+WINDOW_SIZE-1]
    # 이전엔 slice하고 합치는 과정을 매번 해줬는데 이것때매 시간초과 됐음
    # 기존의 값을 최대한 재활용.
    if(tmp>max_value):
        max_value=tmp
        count=1
    elif(tmp==max_value):
        count+=1
    start_point+=1


if(max_value==0):
    print("SAD")
else:
    print(max_value)
    print(count)


"""
시간초과 뜬 풀이
ARRAY_LEN, WINDOW_SIZE = map(int, input().split())
ARRAY = list(map(int, input().split()))

start_point =0
max_value = -1
count = -1
while(start_point+WINDOW_SIZE <= ARRAY_LEN):
    tmp = sum(ARRAY[start_point:start_point+WINDOW_SIZE]) => 이부분이 원인
    if(tmp>max_value):
        max_value=tmp
        count=1
    elif(tmp==max_value):
        count+=1
    start_point+=1


if(max_value==0):
    print("SAD")
else:
    print(max_value)
    print(count)
"""