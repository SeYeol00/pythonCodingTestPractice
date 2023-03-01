import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

# 섹션 3에 있던 사과나무와 똑같지만 BFS로 풀어보겠다.

# 주어진 n을 //2로 정 가운데 좌표(n//2,n//2)를 지정한다.
# 이후 인접한 노드들을 탐색하면서 이동한다.
# 레벨이 같은 것들을 우선 탐색하기 때문에 BFS로 풀자
# 레벨이 같은 상,하,좌,우가 노드가 된다.

#                 (2,2)  레벨은 0
#            /    |    |    \
#           상   우     하    좌
#       (1,2)  (2,3)  (3,2) (2,1)   레벨은 1

# 이런 좌표 이동은 dx와 dy로 미리 좌표에 적용할 계산들을 리스트를 만들어 두자
# 시계방향이다.

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# 방문한 곳을 재방문 안 한다. -> 체크리스트 



dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 좌표 생성
n = int(input())

a =[]

for _ in range(n):
    lst = list(map(int, input().split()))
    a.append(lst)

# 합 초기화
sum = 0
# 방문 리스트
ch = [[0]*n for _ in range(n)]
# 큐 생성
Q = deque()



# 이게 한 세트다 아래에서 똑같이 쓸것
# 맨 위 노드 방문
ch[n//2][n//2] = 1
sum = sum + a[n//2][n//2]
# 큐에 넣기, 노드 자체는 좌표(튜플)로 넣는다.
Q.append((n//2,n//2))

# 레벨 초기화
L = 0


# BFS 로직
# 무한 루프, 후에 탈출할 거임
while True:

    # 정지 조건, 중앙에서 출발하니 n//2의 레벨이 된다는 걸 명심하자
    if L == n//2:
        # 정지
        break

    # 큐의 사이즈를 저장, 현재 레벨의 노드들이 저장되었을 것
    size = len(Q)

    # 현재 레벨 전체의 시퀀스
    # 현재 레벨의 사이즈 * 4 만큼 돌 것이다.
    for _ in range(size):
        temp = Q.popleft()
        for i in range(4):
            # 튜플로 넣었으니까 좌표 입력 가능하다.
            # 좌표 도출
            x = temp[0] + dx[i]
            y = temp[1] + dy[i]
            # 방문 체크
            if ch[x][y] == 0:
                ch[x][y] = 1
                sum += a[x][y]
                Q.append((x,y))

    # 출력
    # print(L,size)
    # for x in ch:
    #     print(x)

    L = L + 1

# 진짜 합 출력
print(sum)
    


