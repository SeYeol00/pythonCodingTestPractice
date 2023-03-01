import sys
sys.stdin=open("input.txt","r")


# 1을 포함한다, 포함하지 않는다.
# 3을 포함한다, 포함하지 않는다.
# .. .. .. .. .
# 부분 집합의 모든 원소의 합을 sum에 저장하자

# 전체 원소의 합을 total이라고 하고
# 부분집합의 합 sum을 total에서 빼주면
# 그것이 나머지 부분집합의 합이다.
# 이게 맞으면 YES

# 부분 집합의 합을 누적하는 변수 = sum
def DFS(L,sum):
    # L은 a라는 리스트를 참조하는 인덱스 번호다.
    # 이진트리 사용으로 Level을 쓰는데 있어 L이란 변수로 지칭할 것이다.
    # 이진트리의 왼쪽 노드는 부모 노드의 원소를 사용할 때 sum에 더해주고
    # 오른쪽 노드는 안 사용할 때 sum에 더해주지 않는다.
    if L == n:
        # Total의 값이 홀수여서 //2를 쓰면 문제가 생긴다.
        if (total - sum) == sum:
            print("YES")
            # 프로그램 종료 코드
            # 아예 메인을 강제 정지 시켜버린다.
            # NO를 도출하는 건 DFS가 끝난 후에 YES가 나오지 않을 때 출력하자
            sys.exit(0)
    # else 코드 안 넣으면 이상해진다.
    else:
        # 핵심 알고리즘
        # 두 갈래로 나누기
        
        # 왼쪽 노드
        DFS(L+1,sum + a[L])
        #오른쪽 노드
        DFS(L+1,sum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    # 총합
    total = sum(a)

    DFS(0,0)
    print("NO")
    
