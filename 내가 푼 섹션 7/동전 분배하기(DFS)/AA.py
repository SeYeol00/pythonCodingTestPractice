import sys
sys.stdin=open("input.txt","r")


# 상태 트리를 먼저 그려보자
# 이게 DFS() 문제라고 생각이 된다면 상태 트리를 그린다.
# 여기서 동전의 갯수 => 레벨이라고 생각하자
# 그럼 상태 트리의 노드가 
# 1. A한테 줄것인지
# 2. B한테 줄것인지
# 3. C한테 줄것인지 
# 이렇게 3개가 된다.
# 리스트 크기가 3인 분배 리스트를 만든다.
# 0번 인덱스는 A, 1번 인덱스는 B, 2번 인덱스는 C
# 이렇게 할당하고 레벨마다 어느 인덱스에 값을 더할 건지 결정한다.
# 이후 max, min 함수를 통해 최대 최소를 구하고 뺀다.
# 그걸 l==n 에서 res로 스위칭한다.

def DFS(l):
    global res
    if l == n:
        cha = max(money) - min(money)
        if cha < res:
            # 세 사람 중 두 명의 값이나 혹은 세 명의 값이 같을 수 있으니
            # 중복을 제거한다.
            temp = set()
            for x in money:
                temp.add(x)
            # len(temp)가 3이어야 서로 다른 금액인 것이다.
            # 단 세 사람의 총액은 서로 달라야 합니다. -> 조건
            if len(temp) == 3:
                res = cha
    else:# 3명이니까 무조건 3
        # 3가지의 상태 트리 노드
        for i in range(3):
            # 백트래킹도 생각하자
            # money 리스트에 coin 리스트 값을 넣는다.
            # 코인의 인덱스가 레벨과 같기 때문에 l을 넣는다.
            money[i]+=coin[l]
            DFS(l+1)
            # 백트래킹, 돈을 취소하는 순간
            money[i]-=coin[l]



if __name__ == "__main__":
    n = int(input())
    money = [0]*3
    coin = list()
    for _ in range(n):
        coin.append(int(input()))
    res = 10000000
    DFS(0)
    print(res)