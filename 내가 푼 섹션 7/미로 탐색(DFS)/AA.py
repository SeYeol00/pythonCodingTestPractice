import sys
sys.stdin = open("input.txt", "rt")


# 출발점에서 도착 지점까지의 가짓수 -> 카운트를 찾는 문제다.
# 즉 최단 거리 문제가 아니라는 것이다.

# 가짓수를 세는 것은 DFS 문제다.

# 가짓수 혹은 노드를 따라 아래로 파고드는 문제  => DFS

# 최단 거리 탐색 혹은 같은 레벨을 우선적으로 보는 문제 => BFS

# 도착 지점까지 도달 후 백트래킹을 통해 위로 올라가서 찾는다. => 체크를 푼다.

# 격자판이나 호수에서 동심원으로 퍼져나간다 => BFS
# 한 곳 방향으로 쭉 간다. => DFS

# 한 번 지나온 길은 방문 안 한다. => 체크리스트 

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# x, y 좌표를 받자
def DFS(x,y):
    global cnt
    if x == 6 and y == 6:
        cnt+=1
    
    else:
        for i in range(4):
            # 초기화 부터 하자
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy] == 0:
                # 방문
                board[xx][yy] = 1
                DFS(xx,yy)
                # 백트래킹
                board[xx][yy] = 0


if __name__ == "__main__":
    board = [list(map(int,input().split())) for _ in range(7)]
    cnt = 0

    # 출발점 방문, 안하면 에러난다.
    board[0][0] = 1

    DFS(0,0)
    print(cnt)



