import sys
sys.stdin=open("input.txt","r")


# 측정이 불가능한 가짓수 = 측정이 가능한 최댓값 - 측정 가능한 가짓수

# 상태트리 -> 1. 왼쪽에 놓을지 , 2. 오른쪽에 놓을지, 3. 안 놓을지 
# 3개의 노드를 가진다.
# 여기서 추로 무게를 뺼 수 있다.
# 가령 추를 왼쪽에 두고 다른 추를 오른쪽에 두면 그 차이를 잴 수 있다.
# 문제의 경우 1 5 7인데 이 경우
# 1 5 7 기본 3개
# 오른쪽에 추를 둔다는 것을 가정하면
# 1 + 7 - 5,  7 - 5,  7 - 1 등등 생성이 된다.
# 즉 추를 왼쪽에 둘건지(더할건지), 추를 오른쪽에 둘건지(뺼건지), 추를 안 둘건지(합에 아무 영향 안 줄 건지)
# 이런 관점으로 봐야한다.

# 0에서 출발, 1그램을 더할까? -> 왼쪽에 둔다.
# 0에서 출발, 1그램을 뺼까? -> 오른쪽에 둔다.
# 0에서 출발, 1그램을 쓰지 말까? -> 안씀
# 다음 레벨, -> 레벨로 다음 추 인덱싱

# 근데 여기서 생각해야하는게 
# -기호가 붙은 무게는 사실 방향을 반대로 본다면 대칭으로 +로 생각 가능하다.
# 즉 중복이 생긴다. 그래서 -기호는 체크 안 해도 된다.

def DFS(L,sum):
    global res
    
    # 레벨이 끝까지 간 경우
    if L == n:
        if 0<sum<=s:
            # 중복이 존재한다. 노드를 거치면서 같은 값이 존재한다.
            res.add(sum)
        
    else:
        # 세가지 노드, 이걸 더할 거냐, 뺼 거냐, 안 쓸 거냐
        # 상태 노드 3갈래
        DFS(L+1,sum+G[L])
        DFS(L+1,sum-G[L])
        DFS(L+1,sum)

    

if __name__ == '__main__':
    n = int(input())
    G = list(map(int,input().split()))
    # 추로 잴수 있는 최댓값
    s = sum(G)
    # set이라는 자료구조, 중복을 제거할 수 있다.
    # 같은 값이 무수히 나올 수 있으니까 세트를 쓰자
    res = set()
    DFS(0,0)
    # 갯수를 셀 떄는len()함수를 쓰자
    print(s - len(res))
    