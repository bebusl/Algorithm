import sys
input = sys.stdin.readline

n , k = map(int, input().split())
P = []
minimum =0 

for i in range(n):
    num = int(input())
    P.append(num)
   

if(not n<2*k):
    for start in range(0,n-k+1):
        check_1 = [0 for i in range(k+1)]
        check_2= [0 for i in range(k+1)]
        for i in range(start,start+k):
            check_1[P[i]]+=1
        for i in range(0,start):
            check_2[P[i]]+=1
        for i in range(start+k,):
            check_2[P[i]]+=1
        if(all(check_1[1:]) and all(check_2[1:])):
            minimum = k
            break

        for end in range(start+k+1,n):
            if(end-start>n-k):
                break
            check_1[P[end-1]]+=1
            check_2[P[end-1]]-=1
            if(check_2[P[end-1]]<0):
                break
            if(all(check_1[1:]) and all(check_2[1:])):
                minimum = end-start

                break
            
            
        if minimum!=0:
            break
            
# if(not n<2*k):
#     for start in range(0,n-k+1):
#         for end in range(start+k,n):
#             if(end-start>n-k):
#                 break
#             if(len(set(P[start:end]))==k and len(set(P[:start]+P[end:]))==k):
#                 minimum = end-start
#                 break
#         if minimum!=0:
#             break
            
print(minimum)
