
def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = bin(number)[2:]
        bin_next_number = bin(number+1)[2:]
        if(bin_number[-1]=='0'):
            answer.append(number+1)
        else:
            rest = len(bin_next_number)
            diffs = bin(number ^ (number+1))[2:]
            diffs = '0' * abs(rest-len(diffs)) + diffs
            bin_number = '0'*abs(rest-len(bin_number))+bin_number

            diff_cnt = diffs.count('1')
            tmp = list(bin_next_number)
            for idx in range(len(diffs)-1,-1,-1):
                if (diff_cnt <= 2):
                    answer.append(int(''.join(tmp), 2))
                    break
                if(diffs[idx]=='1'):
                    diff_cnt-=1
                    tmp[idx] = '0' if tmp[idx] == '1' else '1'



    return answer

print(solution([2,7]),"ANSWER : [3,11]")

# 프로그래머스 77885 bit
# 다른 사람 풀이 많이 봐야할듯 함!
# 짝수는 끝이 0이므로 그냥 1더한 것 바로 반환
# 끝이 홀수 일 때는 1을 더하고 xor연산을 해서 다른 비트를 찾음
# 뒤에서 부터 다른 비트 개수가 2개 이하가 되도록 xor이 1인 부분은 원본