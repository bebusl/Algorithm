from sys import stdin
import re
input = stdin.readline

def solution(test):
    tmp = test.replace(' ','')
    tmp = tmp.lower()
    p = re.compile('[a-z0-9]')  #숫자인지 문자인지 판단할 정규표현식
    tmp = ''.join(filter(lambda x:x if bool(p.match(x)) else False,tmp))
    for i in range(len(tmp)//2):
        if(tmp[i]!=tmp[len(tmp)-1-i]):
            return False
    return True

def good_solution(test):
    tmp = test.lower()
    tmp = re.sub('[^a-z0-9]','',tmp) #이건 문자와 숫자가 아닌건 다 삭제하는 부분
    
    return tmp==tmp[::-1] #

test= "race a car"
"""
    race a car
"""

print(solution(test))