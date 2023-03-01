import sys
sys.stdin=open("input.txt","r")



# 방문 체크 리스트 , 인접 행렬 두 개가 필요하다.
# 경로 탐색은 DFS()를 사용해야한다.

def DFS(v):
    global cnt
    # 목적 노드에 도착했다면 DFS() 정지
    if v==n:
        cnt+=1

        # 도착했을 때 경로 리스트에 저장된 노드를 다 뽑자
        for x in path:
            print(x, end=" ")
        print()

    else: # 가지(상태 노드) 뻗기
        for i in range(1,n+1): # i가 방문하려는 노드다. 1부터 5까지
            # 방문 로직
            # 인접행렬이 연결이 되어있습니까?
            if g[v][i] == 1:
                if ch[i] == 0:
                    ch[i] = 1

                    # i로 가야하니까 i를 경로 리스트에 추가
                    path.append(i)
                    DFS(i)

                    # 백트래킹
                    path.pop() # 넣었던 거 다시 빼야 백트래킹 된다.
                    ch[i] = 0


if __name__=='__main__':
    n,m = map(int, input().split())

    # 인접 리스트 생성
    g = [[0]*(n+1) for _ in range(n+1)]

    # 방문 체크 리스트 생성
    ch = [0]*(n+1)

    for i in range(m):
        a,b = map(int,input().split())
        # 방향 그래프니까 a,b만. 중요!
        g[a][b] = 1

    cnt = 0

    # 방문 경로 
    path = []

    # 방문 시작 노드는 체크해주자
    ch[1] = 1
    path.append(1)
    DFS(1)
    print(cnt)


