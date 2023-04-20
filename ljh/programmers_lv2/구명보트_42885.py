# 투 포인터

def solution(people, limit):
    answer = 0
    people.sort()

    start = 0
    end = len(people)-1
    while (True):
        # start == end이면, start는 아예 안 움직이고 end만 앞으로 온 것이므로 start는 혼자 남게 된다 => +1해야 함
        if (start == end):
            answer += 1
            break
        # start > end 이면 start+end값이 한 쌍을 이뤄 보트를 탔다는 뜻. 그래서 다음 Index가 서로 교차하게 된다 => start는 +1, end는 -1이므로 필연적으로 start가 커지게 된다.
        if(start>end):
            break
        start_end_sum = people[start] + people[end]
        if (start_end_sum <= limit):
            start += 1
            answer += 1
        else:
            answer += 1
        end-=1

    return answer

print(solution(	[70, 50, 80, 50],100))
print("정답 : ",3)
print("==============================")
# 1. [40, 40, 40, 40, 50], 200 => 3
# 몸무게 제한을 반절로 나눈 값을 기준으로 사람들을 나눴을 때, 더 무거운 그룹에 한 명도 없는 경우입니다. 빈 그룹에서 사람을 호출하려고 할 때 런타임 에러가 생깁니다.

# 2. [60, 60, 51, 51, 100], 100 => 5
# 더 가벼운 그룹에 한 명도 없는 경우입니다. 마찬가지로 빈 그룹에서 사람을 호출하는 코드가 있다면 런타임 에러가 발생합니다.

# 3. [40], 40 => 1
# 사람이 한 명 뿐인 경우. 필연적으로 위의 두 가지 문제 중 하나가 생깁니다. 그냥 처음에 1을 반환해버리면 편합니다.

# 4. [40, 55, 55, 60, 60, 60, 70, 80], 100 => 7