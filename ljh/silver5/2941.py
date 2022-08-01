import sys
input = sys.stdin.readline

words = input().strip("\n")

# 첫번째 답. 맞긴한데 효율 엄청 떨어짐.
# croatia = {"c":["=",'-'],"d":["z=","-"],"l":["j"],"n":["j"],"s":["="],"z":["="]}
# croatia_keys = croatia.keys()
# cnt=0

# idx=0
# while(idx<len(words)):
#     isCroatian =False
#     if words[idx] in croatia_keys:
#         for t in croatia[words[idx]]:
#             if(words[idx+1:idx+len(t)+1]==t):
#                 cnt+=1
#                 idx+=len(t)
#                 idx+=1
#                 isCroatian=True
#                 break
#     if(isCroatian):
#         continue
#     cnt+=1    
#     idx+=1
        
# print("RESULT",cnt)

# 두번째답. 마찬가지로 효율 엄청 떨어짐.
croatia = ["c=","c-","d-","lj","nj","s=","z="]
cnt=0
idx =0
while(idx<len(words)):
    if(words[idx:idx+3] == "dz="):
        cnt+=1
        idx+=3
    else:
        if words[idx:idx+2] in croatia:
            idx+=1
        cnt+=1
        idx+=1
print(cnt)

##마음에 드는 해답. 알파벳으로 표현한거 다 한글자로 변경해서 최종 스트링 길이만 반환하면 끝!
# m=["c=","c-","dz=","d-","lj","nj","s=","z="]
# s=str(input())
# for i in m:
#     s=s.replace(i,"a")    
# print(len(s))