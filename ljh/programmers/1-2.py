def solution(s, n):
    answer = ''
    for i in s:
        if(i == ' '):
            answer+=' '
            continue
        value = ord(i)+n
        if(value>=123):
            value -= 123
            value += 97          
        elif(91<=value<=96):
            value -= 91
            value += 65
        answer+=chr(value)
    return answer
    
    
print("RESULT :: ",solution('a B z',4))