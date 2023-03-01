import sys
sys.stdin=open("input.txt","r")


# 최대 부분 증가수열과 같은 맥락
# 메모 리스트 필요

# 벽돌의 무게, 밑면 넓이, 높이 3개의 인수들이 정렬이 되어야한다.
# 가장 높은 탑을 쌓는 방법 => 최대부분 증가 수열
# 넓이, 높이, 무게를 묶어서 작은 리스트로 받고
# 그걸 큰 리스트에 넣는다.
# 즉 0번 벽돌, 1번 벽돌, 2번 벽돌 ... 이렇게 리스트를 구현한다.
# 밑면 넓이를 기준으로 한 번 소팅하자
# 이러면 벽돌이 0번 부터 끝번까지 차례로 쌓게 된다.
# 이러면 밑면은 볼 필요가 없다. 밑면 조건을 만족시킨다.
# 밑면은 보지 말자

# 결국 문제에서 여러 기준이 존재한다면
# 어찌보면 그리디라고 보면 된다.
# 한 가지 기준을 만족시키고 들어가야한다.

# 다음으로 무게를 고려해야한다.
# 이 때 다이나믹 프로그래밍을 적용시킨다.


if __name__ == "__main__":
    n = int(input())

    bricks = [list(map(int, input().split())) for _ in range(n)]

    # 밑면 넓이 고려는 끝
    bricks.sort(key=lambda x: x[0],reverse=True)
    print(bricks)

    # memo[2]는 제일 꼭대기에 2번 벽돌을 둔다는 가정하의 높이
    # memo[4]는 제일 꼭대기에 4번 벽돌에 놓았다고 가정했을 때의 높이
    # 여기서는 memo[0]에 bricks 0번을 넣고 시작하자
    memo = [0] * (n)
    # 1번에 높이가 들어가 있으니까
    memo[0] = bricks[0][1]

    res = 0
    
    # 디피 최대부분 증가수열 시작
    for i in range(1,n):
        max = 0
        # 앞을 봐야된다.
        # 인덱스가 -1이면 0까지 돌아라
        for j in range(i-1,-1,-1):
            if bricks[j][2] > bricks[i][2]:
                # 무조건 메모 검증을 해야한다. 메모이제이션
                if memo[j] > max:
                    # i 전에 있던 최대 값들 중 가장 큰 값 찾기
                    max = memo[j]
        # 여기에서 값을 더해둘 것이다.
        memo[i] = max + bricks[i][1]
        if memo[i] > res:
            res = memo[i]

    print(res)
