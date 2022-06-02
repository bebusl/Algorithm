# 선택 정렬
# 아직 정렬되지 않은 남은 것들 중 최소값을 가져와서 정렬된 곳의 맨 마지막에 끼워넣음

def selection_sort (array=[7,5,9,0,3,1,6,2,4,8]):
    for i in range(len(array)):
        min_index  = i
        for j in range(i+1, len(array)):
            if array[min_index]>array[j]:
                min_index = j #남은 것 중 가장 작은 값이 있는 곳의 인덱스 저장.
        array[i],array[min_index]=array[min_index],array[i] # 값 스와이프.
    
    print(array)
        
#삽입정렬
#칸을 하나씩 늘려가면서, 아직 정렬되지 않은 값의 위치를 찾아 삽입하는 것
def insert_sort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j]<array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
            else:
                break
            
    print(array)

#퀵 정렬
#pivot 기준. pivot보다 작은 값 => pivot 왼쪽으로. pivot 보다 큰 값 => pivot 오른쪽으로
def quick_sort(array,start,end):
    if start>=end: #원소가 1개인 경우 종료
        return
    pivot = start
    left = start+1
    right = end
    while left<=right:
        while left<= end and array[left] <= array[pivot]:
            left +=1
        while right>start and array[right] >=array[pivot]:
            right -=1
        if left>right: #엇갈렸다! 
            array[right],array[pivot]= array[pivot],array[right]   
        else:
            array[left],array[right]= array[right],array[left]
        
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
    
    print(array)

#파이썬 친화적인 퀵소트
def pythonic_quick_sort(array):
    if len(array) <=1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]
    
    return pythonic_quick_sort(left_side)+[pivot]+pythonic_quick_sort(right_side)
    


test_array = [7,5,9,0,3,1,6,2,4,8]
# selection_sort()
#insert_sort(test_array)
#quick_sort(test_array,0,len(test_array)-1)
print(pythonic_quick_sort(test_array))