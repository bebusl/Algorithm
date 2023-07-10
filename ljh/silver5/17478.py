N = int(input())
def solution(depth=0):
    prefix = "____"*depth

    print(prefix + '"재귀함수가 뭔가요?"')
    if(depth>=N):
        print(prefix+'"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(prefix+"라고 답변하였지.")
        return
    print(prefix + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(prefix + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print(prefix + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    solution(depth+1)
    print(prefix+"라고 답변하였지.")
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
solution()

"""문제를 잘 읽자..!
global 키워드 쓰면 성능이 확 떨어지더라. 전역변수의 내용을 내부 함수에서 변경해야 하는 게 아니라면 global키워드 사용은 자제할 것"""
