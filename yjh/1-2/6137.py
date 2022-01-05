N = int(input())

arr = ''
for i in range(N):
    arr += input()

start, end = 0, N - 1
len = 0
while start <= end:
    if ord(arr[start]) < ord(arr[end]):
        print(arr[start], end='')
        start += 1
    elif ord(arr[start]) > ord(arr[end]):
        print(arr[end], end='')
        end -= 1
    else:
        temp_start, temp_end = start, end
        front = False
        while ord(arr[temp_start]) == ord(arr[temp_end]):
            if temp_start < N - 1:
                temp_start += 1
            if temp_end > 0:
                temp_end -= 1
            if ord(arr[temp_start]) < ord(arr[temp_end]):
                front = True
            else:
                front = False
        if front:
            print(arr[start], end='')
            start += 1
        else:
            print(arr[end], end='')
            end -= 1

    len += 1
    if len % 80 == 0:
        print()