import re

"""
PROB. 로그 파일 재정렬(릿코드 937)
로그를 재정렬. 정렬 기준은 아래와 같음.
1. 로그의 가장 앞 부분 = 식별자
2. 문자로 구성된 로그가 숫자로그보다 앞에 와야 함.
3. 식별자는 순서에 영향x 단, 문자가 동일한 경우에는 식별자 순으로 정렬.
4. 숫자 로그는 무조건 입력 순서대로!(python 3.7이상부터는 dictionary의 order가 보장됨.)
"""
def solution(logs):
    char_log=[]
    dig_log=[]
    is_digit_log = re.compile(r"^\d+$") 
    for log in logs:
        print(log)
        tmp = log.split()
        if(is_digit_log.match(tmp[1])): #숫자 로그일 경우
            dig_log.append(' '.join(tmp))
        else:
            char_log.append(tmp)
    char_log = sorted(char_log,key=lambda x:(x[1:],x[0]))
    char_log = list(map(lambda y : ' '.join(y),char_log))
    return char_log+dig_log

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
expected_output = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

result = solution(logs)

print("RESULT : ",result)
print(result==expected_output)

