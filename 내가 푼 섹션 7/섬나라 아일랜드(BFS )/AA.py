import sys
from collections import deque
sys.stdin=open("input.txt","r")

# 12시 방향을 기준으로 시계방향
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]


# 이 문제는 BFS로 8방향, 즉 대각선도 탐색한다.
# 섬이 몇 개 있는가, 동떨어진 지역을 세는 문제는 BFS의 경우 8방향을 탐색한다.
# 갯수만 세면된다. 전 문제 단지 번호붙이기 생각을 하자

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

# 섬의 갯수
cnt = 0

# 큐
Q = deque()

# 섬이나 기타 영역 갯수를 세는 문제는 값이 1인 좌표를 찾는 것부터 시작한다.
# 단지 번호 붙이기를 생각하자
for i in range(n):
    for j in range(n):
        # 값이 1인 곳을 방문
        if board[i][j] == 1:
            # 방문한 곳을 체크
            board[i][j] = 0
            # 방문한 곳의 좌표를 큐에 넣는다.
            # 튜플로 넣는다.
            Q.append((i,j))
            while Q:
                temp = Q.popleft()
                # 8방향
                for k in range(8):
                    xx = temp[0] + dx[k]
                    yy = temp[1] + dy[k]
                    if 0<= xx < n and 0<= yy < n and board[xx][yy] == 1:
                        board[xx][yy] = 0
                        Q.append((xx,yy))
            # 영역의 갯수를 세는 문제는 DFS 혹은 BFS가 한 번 끝났을 때 카운팅한다.
            cnt+=1
print(cnt)

                                        
    
