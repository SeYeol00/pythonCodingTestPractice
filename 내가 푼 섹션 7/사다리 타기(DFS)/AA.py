import sys
sys.stdin=open("input.txt","r")


# 어떤 열에서 출발해야 올바른 곳에 도착할까
# -> 도착점부터 출발해서 역으로 DFS를 한다. 
# 아래에서부터 위로 올라가서 마지막 행에 위치한 출발지의 열을 도출한다.
# board = 격자 정보
# dfs로 호출

# x값이 0이 되면 도착, print(y)

# board 9행에서 열만 탐색
# 왼쪽과 오른 쪽을 먼저 보고 그 다음에 위를 본다.
# 사다리 타기는 오른쪽과 왼쪽에 연결된 지점으로 위치가 바뀌기 때문이다.
# ch 체크리스트를 만든다.
# 체크가 안되어있는 좌표로 이동한다.
# board[x][y]에서 x가 0되는 지점에서 y를 도풀

def DFS(x,y):
    # 방문
    ch[x][y] = 1

    if x == 0:
        print(y)
        return
        # 왼쪽 오른쪽이 우선적
    else:   # 경계선 안이고, 왼쪽으로 갈 노드의 값이 1이고, 방문을 안 했을 때
        if 0<=y-1  and board[x][y-1] == 1 and ch[x][y-1] == 0:
            DFS(x,y-1)
            # 경계선 안이고, 오른쪽으로 갈 노드의 값이 1이고, 방문을 안 했을 때
        elif y+1<10  and board[x][y+1] == 1 and ch[x][y+1] == 0:
            DFS(x,y+1)
            # 경계선 안이고, 위쪽으로 갈 노드의 값이 1이고, 방문을 안 했을 때
        elif x-1 >=0 and board[x-1][y] == 1 and ch[x-1][y] == 0:
            DFS(x-1,y)
        



if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0]*10 for _ in range(10)]
    # 마지막 행의 열만 뒤져야한다.
    for y in range(10):
        if board[9][y] == 2:
            DFS(9,y)