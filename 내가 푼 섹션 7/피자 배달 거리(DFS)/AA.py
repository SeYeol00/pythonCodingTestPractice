import sys
sys.stdin=open("input.txt","r")

# board에 들어오는 값들 저장
# 집은 hs라는 리스트에 좌표 저장 hs =[(x1,y1),(x2,y2)...]
# 피자 가게는 pz라는 리스트에 좌표 저장 pz =[(x1,y1),(x2,y2)...]
# 이 문제는 조합 문제다
# 현재 들어오는 피자가게는 6개 그 중 4개를 m으로 받아 살린다.
# 즉 상태트리를 구성해서 조합으로 만드는 것이다.
# 조합 dfs에 거리 구하는 것만 추가하면 된다.
# 피자집 리스트의 인덱스 만큼 재귀를 돌린다.

# DFS에서 필요한 인수 -> 레벨, 넘길 값
# 이 DFS는 조합용 DFS
def DFS(L,s):
    global res
    # m개 뽑았을 때
    if L==m:
        sum = 0 # 도시의 피자 거리
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1-x2)+ abs(y1-y2))
            sum += dis
        if sum<res:
            res = sum
    else:# 조합은 s부터 시작한다. 뽑은 인덱스는 안 뽑는 거임
        for i in range(s,len(pz)):
            cb[L] = i
            DFS(L + 1 , i + 1)


# =================================================
        # for i in range(len(pz)):
        #     dis = abs(hs[i][0] - pz[i][0]) + abs(hs[i][1] - pz[i][1])
        #     if dis < res:
        #         res = dis


if __name__ == "__main__":
    n,m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    pz = []
    hs = []

    # 조합 리스트, 6개 중에 뭘 고를 것인가, 고른 걸 저장하기 위한 리스트
    cb = [0]*m

    # 최대 정수
    res = 2147000000

    # 집이랑 피자 가게를 찾자
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i,j))
            elif board[i][j] == 2:
                pz.append((i,j))
    # 자료 준비 완료


    # 시작은 0레벨에 0번 인덱스
    DFS(0,0)

    print(res)
