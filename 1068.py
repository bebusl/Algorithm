"""
sample
5
-1 0 0 1 1
2
"""
import sys
from collections import defaultdict 
input = sys.stdin.readline

n = int(input())
tree = [-2,]
tree_=defaultdict(list)
tree.extend(list(map(lambda x: int(x)+1, input().split())))
deleted = int(input())+1

def search(index):
    global tree_
    if index == deleted:
        return 0
    else :
        if not index in tree_:
            return 1
        temp = 0
        if(len(tree_[index])==1 and deleted==tree_[index][0]):
            return 1
        for i in tree_[index]:
            temp += search(i)
        return temp

for i in range(1, n+1):
    tree_[tree[i]].append(i)

print(search(tree_[0][0]))

