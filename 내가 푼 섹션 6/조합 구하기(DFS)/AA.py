import sys
sys.stdin=open("input.txt","r")

# 이 문제를 베이스로 해서 많은 문제들이 출제된다.
# 조합 중요하다.
# 순열과 비슷한 코드지만 상태 트리가 다르다.

#   L S
# D(0,1)
# 상태트리의 자식 노드는 4개
# 자식 노드의 for문은 S부터 돈다.

# 그래서 다음 자식 노드는 D(레벨 1, S+1부터 끝까지의 인수의 for문 i값이 된다.)

def DFS(L,S):
    global cnt
    if L==m:
        # 레벨이 2로 갔을 때
        for j in range(L):
            print(res[j],end=' ')
        cnt+=1
        print()
    else: # S부터 n+1까지
        for i in range(S,n+1):
            res[L]=i
            # 가지가 뻗는 것은 i므로 i+1을 해야한다.
            DFS(L+1,i+1)


if __name__ == "__main__":
    n,m = map(int, input().split())
    res = [0] * (n+1)
    cnt = 0
    # 레벨을 res의 인덱스로 사용할 것이다.
    DFS(0,1)
    print(cnt)


