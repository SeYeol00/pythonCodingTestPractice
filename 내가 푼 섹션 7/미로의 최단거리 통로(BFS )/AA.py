import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

# 최단 거리는 무조건 BFS 넓이 우선 탐색으로 푼다.

# 입력 데이터는 board라는 2차원 리스트에 받는다.

# 출발점을 0으로 초기화한다.

# 좌표를 이동하는 문제니 같은 레벨을 비교하는 BFS()로 푼다.
# 좌표 이동 문제 -> dis, ch 리스트 생성

# dis 리스트는 이동 거리 저장용
# ch는 방문 체크 리스트

# 출발점의 오른 쪽을 갈 수 있다. 혹은 아래 쪽을 갈 수 있다. => 이동 거리 + 1


dx = [-1,0,1,0]
dy = [0,1,0,-1]

board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]
Q = deque()
# 출발점
Q.append((0,0))

# 여기서는 방문 체크 리스트를 안 만들고 방문한 곳을 벽으로 만들 것이다.
board[0][0] = 1
while Q:
    tmp = Q.popleft()
    # 4 방향 탐색
    for i in range(4):
        # tmp는 튜플
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        # 경계선 밖으로 안 나가려면 아래 조건을 달아줘야한다.
        if 0<=x<=6 and 0<=y<=6 and board[x][y] == 0:
            # 방문 체크
            board[x][y] = 1
            # 이동 거리 갱신
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            # 큐에 넣기
            Q.append((x,y))

# 벽에 막혀서 출력 불가, 루트가 없다. -> 목적지의 이동 거리 갱신이 안 됐다.
if dis[6][6] == 0:
    print(-1)
# 도착!
else:
    print(dis[6][6])