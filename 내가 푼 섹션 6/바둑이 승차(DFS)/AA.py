import sys
from collections import deque
sys.stdin=open("input.txt","r")


# 부분집합 -> DFS 
# 이 문제도 부분집합 문제이다.
# 즉 DFS를 통해 여러 갈래로 부분집합이 생기는데
# 이 부분 집합 케이스를 

# l이 리스트에 접근하는 인덱스 번호
def DFS(l,sum,tsum):

    # 값을 저장할 곳
    global result


    # 정지 코드
    if sum + (total - tsum) < result:
        return

    # 정지 코드
    if sum > c:
        return
    if l == n: # 맨 마지막 레벨까지 간 것
        # 답 도출용
        # 부분집합이 하나 완성된것, 레벨이 n과 같으면 끝에 왔다.
        # 가지를 계속 뻗어 나가는 것
        if sum > result:
            result = sum
    else: # 부분집합 빠져나가기
        # 핵심 알고리즘
        # 두 갈래로 나누기
        
        # 포함 시킬건지 안 포함 시킬건지
        # 가지 처럼 뻗어나간다고 생각하자.

        # 왼쪽 노드, 지금 노드를 넣는다.
        DFS(l+1,sum+weights[l],tsum+weights[l])
        #오른쪽 노드, 넣지 않는다.
        DFS(l+1,sum,tsum+weights[l])


if __name__ == "__main__":
    c,n = map(int,input().split())

    weights = [0]*n

    #정답
    result = 0
    #인덱스로 접근할 거다.
    for i in range(n):
        weight = int(input())
        weights[i] = weight
    total = sum(weights)
    # weights.sort()
    # print(weights)
    
    DFS(0,0,0)
    print(result)