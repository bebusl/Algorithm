import sys
from collections import deque
import copy
input = sys.stdin.readline

A, B, C, D = input().split()
#isWin = [+3, +1, 0] # 우승, 비김, 짐
queue = deque()
cnt=3
tmpcnt=0
for i in range(6):
    case = input().split()
    case[2:]=map(float, case[2:])
    #A,B win same loose
    if i ==0  :
        cnt = 0
        if(case[2]>0):
            score = {A : 0,B: 0,C:0,D:0}
            score[case[0]]+=3
            score["percent"]=case[2]
            queue.append(score)
            cnt+=1
        if(case[3]>0):    
            score = {A : 0,B: 0,C:0,D:0}
            score[case[0]]+=1
            score[case[1]]+=1
            score["percent"]=case[3]
            queue.append(score)
            cnt+=1
        if(case[4]>0):
            score = {A : 0,B: 0,C:0,D:0}
            score[case[1]]+=3
            score["percent"]=case[4]
            queue.append(score)
            cnt+=1
        # print("1" , queue)
    else:
        tmpcnt = 0
        for j in range(cnt):
            score = queue.popleft()
            if(case[2]>0):
                temp =copy.deepcopy(score)
                temp[case[0]]+=3
                temp["percent"]*=case[2]
                queue.append(temp)
                tmpcnt+=1
            
            if(case[3]>0):
                temp =copy.deepcopy(score)
                temp[case[0]]+=1
                temp[case[1]]+=1
                temp["percent"]*=case[3]
                queue.append(temp)
                tmpcnt+=1            
            
            if(case[4]>0):
                temp =copy.deepcopy(score)
                temp[case[1]]+=3
                temp["percent"]*=case[4]
                queue.append(temp)
                tmpcnt+=1
        cnt=tmpcnt
        
print(queue)
finalscore=[0,0,0,0]
for i in queue:
    score =[
        i[A],i[B],i[C],i[D]
    ]
    percent = i["percent"]
    sorting_rate = sorted(score,reverse=True)
    if(score.count(sorting_rate[0])>=2): # 1등 동점자가 2명이상인경우
        pos = [ i for i in range(4) if score[i]==sorting_rate[0]]
        percent = percent*(2/len(pos))#동점자중 2명 뽑는거
        for i in pos:
            finalscore[i] += percent
    elif(score.count(sorting_rate[0])==1 and score.count(sorting_rate[1])>=2): # 1등 한명, 2등 동점자가 있는 경우 2등 동점자 중 한 명
        pos = [i for i in range(4) if score[i]==sorting_rate[1]]
        for i in pos:
            finalscore[i] += percent*(1/len(pos))
        finalscore[score.index(sorting_rate[0])]+=percent
    elif(score.count(sorting_rate[0])==1 and score.count(sorting_rate[1])==1): # 1등, 2등 한명씩만 있을 경우
        finalscore[score.index(sorting_rate[0])] += percent
        finalscore[score.index(sorting_rate[1])] += percent       

for i in range(4):
    print(finalscore[i])

