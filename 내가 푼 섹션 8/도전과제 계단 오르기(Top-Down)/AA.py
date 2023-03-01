import sys
sys.stdin=open("input.txt","r")


# 사실 동적 계획법은 Bottom-Up이 진짜다.
# Top-Down은 넓은 의미의 동적 계획법이고
# 좁은 의미로는 결국 재귀함수다.
# 재귀함수에서 커팅 엣지를 실시하는 것


def DFS(len):
    if len == 1 or len == 2:
        return len

    # 커팅 엣지
    if memo[len] != 0:
        return memo[len]

    else:
        memo[len] = DFS(len -1) + DFS(len -2)
        return memo[len]


if __name__ == "__main__":
    n = int(input())
    # 메모 리스트
    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 2
    
    print(DFS(n))