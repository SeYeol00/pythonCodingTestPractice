import sys
from collections import deque
sys.stdin=open("input.txt","r")

# 토마토 창고에 있는 정보
# board라는 2차원 리스트에 지도 정보 저장
# dis라는 같은 크기의 빈 2차원 리스트 
# 여기에 몇 일 만에 모든 박스가 썩는지 저장할 것임
# 원리는 결국 일반 dis와 같다.
# 방문하면 board의 값을 1로 바꾸어 저장한다.
# dis 리스트에 들어가는 값을 날짜라고 생각해도 된다.
# board를 2차원 탐색을 한다.
# 익은 토마토의 값을 큐에 넣는다.
# 큐에 익은 토마토의 위치를 다 넣는다.
# dx, dy 즉 4방향을 생각하자.
# 익은 토마토의 위치 튜플들을 큐에 넣어서 탐색한다.
# dis는 처음 위치는 0, 그 다음에 큐에서 나온 좌표들을 통해
# board에서 만약 x는 0..4, y는 0..6이고 방문 안 했고 board의 값이 -1아니면
# 방문!! 즉 보드[x][y]의 값을 1로
# 상태 트리로 뻗는다
# 첫 부모는 0일에서 이미 익은 것들
# 다음 상태 트리 레벨은 1일 째에 익은 것들
# 그 다음 상태 트리 레벨은 2일 째에 익은 것들
# 이렇게 4방향 탐색으로 다음 레벨 노드들을 큐에 넣으면서 돌린다.
# 그 와중에 dis에 같은 좌표들의 값을 전 노드의 dis위치 값 +1을 한다.

dx = [-1, 0 ,1, 0]
dy = [0,1,0,-1]

n,m = map(int, input().split())

board = [list(map(int,input().split())) for _ in range(m)]

dis = [[0]*n for _ in range(m)]

Q = deque()

# 이중 for문을 돌면서 이미 익은 토마토를 찾는다.
# 행을 먼저 둬야한다. 조심!
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i,j))

# BFS 코드
# 찾고 바깥에서 뒤져야한다.
# 좌표만 찾을 거였다.
while Q:
    temp = Q.popleft()

    for i in range(4):
        x = temp[0] + dx[i]
        y = temp[1] + dy[i]

        # bfs나 dfs나 경계선을 지키자
        if 0<=x<m and 0<=y<n and board[x][y] == 0:
            # 방문
            board[x][y] = 1
            dis[x][y] = dis[temp[0]][temp[1]] + 1
            Q.append((x,y))
# 탐색 끝
# 모든게 익었는지 확인해야한다.
flag = 1
for i in range(m):
    for j in range(n):
        # 안 익은 토마토가 있으면
        if board[i][j] == 0:
            flag = 0

result = 0
if flag == 1:
    # 최소 일 수 찾기
    for i in range(m):
        for j in range(n):
            if dis[i][j] >result:
                result = dis[i][j]
    print(result)
else:
    print(-1)


