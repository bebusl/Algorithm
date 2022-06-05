from sys import stdin
from collections import Counter
import re

def sub(x):
    regex = re.compile(r"[^\w]") #숫자나 문자가 아닌 것.
    result = regex.sub('',x.lower())
    return result 

def my_solution(paragraph, banned):
    text = list(map(sub,paragraph.split()))
    text = list(filter(lambda x : x if x not in banned else None, text))
    most_common = Counter(text)
    print(most_common.most_common(1)[0][0])

def best_solution(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]',' ',paragraph)
             .lower().split()
             if word not in banned]
    # list comprehension
    # 첨부터 리스트 컴프리헨션 이용하면 위에 내 솔루션처럼 map, filter 두번 반복시킬 필요 X
    counts = Counter(words)    
    print(counts.most_common(1)[0][0])


test_paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
test_ban=["hit"]

my_solution(test_paragraph, test_ban)
best_solution(test_paragraph, test_ban)