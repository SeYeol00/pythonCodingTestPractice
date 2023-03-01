import sys
sys.stdin=open("input.txt","r")

# 핵심은 입력 정보를 그래프화 시키는 것이다
# 들어오는 정보를 인접행렬로 정리하자




if __name__ == "__main__":
    
    n = int(input())

    # 플로이드 와샬은 항상 최단거리를 기준으로 하기 때문에 최소 비용을 구하는 로직이다.
    board = [[100]*(n+1) for _ in range(n+1)]

    for i in range(n+1):
        board[i][i] = 0

    res = [0] * (n+1)

    while True:
        a,b = map(int,input().split())

        if a == -1 and b == -1:
            break
        
        # 양방향 그래프이기 때문에 둘 다 넣어주자
        board[a][b] = 1
        board[b][a] = 1
    

    # 친구의 친구 == 플로이드 와샬을 쓰자

    # 중간에 거치는 노드 k가 필요하기 때문에 결국 3중 for문을 돌아야 한다.
    # k가 들어가는 것은 친구의 친구를 뜻한다.
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if board[i][j] > board[i][k] + board[k][j]:
                    board[i][j] = board[i][k] + board[k][j]


    for x in range(n+1):
        print(board[x])

    for i in range(1,n+1):
        large = max(board[i][1:])
        res[i] = large

    # 회장 후보가 될수있는 점수
    score = min(res[1:])
    print(score)

    # 회장이 될 수 있는 사람들의 인원
    out = []
    
    for i in range(1,n+1):
        if res[i] == score:
            out.append(i)

    print(f"{score}, {len(out)}")
    
    # 후보인 사람들 보기
    for x in range(len(out)):
        print(out[x], end=' ')