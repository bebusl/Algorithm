from collections import deque

left_str = deque(input())
right_str = deque()
instruct_num = int(input())

# L일떄
for i in range(instruct_num):
  instruction = input()
  if (len(instruction) > 1):
    left_str.append(instruction[-1])
  elif (instruction == 'L'):
    if (len(left_str) > 0):
      tmp = left_str.pop()
      right_str.appendleft(tmp)
  elif (instruction == 'D'):
    if (len(right_str)>0):
      tmp = right_str.popleft()
      left_str.append(tmp)  
  else:
    if (len(left_str)>0):
      left_str.pop()

print(''.join(left_str)+''.join(right_str))
