order = [1,2,3,4,5]
SELECT_NUMBER = 3
select = [ False for i in order]


def print_combi():
    for i,item in enumerate(order):
        if select[i]:
            print(item, end=' ')
    print()


def dfs_combi(idx, cnt):
    if cnt == SELECT_NUMBER:
        print_combi()
        return

    for i in range(idx,len(order)):
        if select[i]: continue
        select[i] = True
        dfs_combi(i+1  , cnt+1)
        select[i] = False

order = list(set(order)) # 배열에서 중복된 값 미리 제거
# dfs_combi(0,0)
""" 중복을 불허하는 조합! """


permutaion = []

def print_permutaion():
    print(' '.join(map(str,permutaion)))

def dfs_permutation(cnt):
    if cnt == SELECT_NUMBER:
        print_permutaion()
        return
    for i in range(len(order)):
        if order[i] in permutaion: continue # 중복되는 건 삭제!
        permutaion.append(order[i])
        dfs_permutation(cnt+1)
        permutaion.pop()

dfs_permutation(0) # 중복을 불허하는 순열