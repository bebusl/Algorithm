import re
from collections import Counter

def solution(s):
    numbers = re.sub('[{} ]','',s)
    numbers = list(map(int, numbers.split(',')))
    count = Counter(numbers)
    result = [i for i in map(lambda x: x[0],count.most_common())]

    return result

# 12월 29일