import sys,math
import itertools as it
sys.stdin=open("input.txt","r")


# 수열에 규칙이 존재한다.
# 맨 처음과 맨 끝은 한 번만 더해진다.
# 중간에 있는 것은 3개 씩 더해진다.
# => 이항계수의 규칙이 존재한다.
# 그래서 리스트를 두 개 만들어 각 자리에 매치시켜 곱한다는 개념이다.
# 첫번쨰 리스트에는 계수들의 집합
# 두번째는 순열로 소합할 원소들의 집합
# 이 두 리스트를 매치 시켜 곱하기만 하면 값이 나온다.
# 이항 계수 리스트를 초기화만 잘하면 된다.
# 이항 계수 리스트의 값은 각각 
# 3C0, 3C1, 3C2, 3C3 이렇게 되는데

# 이게 결국  각각 (n-1)C(index)가 되는 것이다.

# 사전의 바로 앞에 오는 건 결국 맨 앞이 된다.
# 우리가 했던 순열이 1부터 n까지므로 사전적으로 하는 것이 된다.

# 라이브러리를 사용한 방법 2
# 다만 라이브러리에 의존하지 말자 코테 막아둔다.

n,f = map(int,input().split(' '))
b = [1] * n
for i in range(1,n):
    b[i] = b[i-1]*(n-i)/i
a = list(range(1,n+1))
# 여기까지 리스트 초기화s

# 중요
# 순열 구하는 라이브러리 초기화, a로 생길 수 있는 모든 순열을 뽑아준다.
# 앞 원소가 작은 것부터 계속 나옴 , a로 만들 수 있는 순열 중 원소 3개 짜리들
for temp in it.permutations(a):
    sum=0 # enumerate -> 인덱스와 값을 동시에 접근이 가능하다.
    # L(인덱스)를 뽑는 이유는 b에 담긴 원소들을 곱하기 위해서이다.
    for L,x in enumerate(temp):
        sum+=(x*b[L])
    if sum == f:
        for x in temp:
            print(x, end=" ")
        break








# 방법 1

# def DFS(l,sum):
#     # 종료 조건, 끝에 다다르고 sum이 f와 같아야 올바른 순열 조합이다.
#     if l ==n and sum == f:
#         for x in permutation:
#             print(x, end= " ")
#         sys.exit() # 첫줄만 뽑고 강제 종료

#     else:
#         for i in range(1,n+1):
#             # 방문 리스트 체크
#             if check[i] == 0:
#                 check[i] = 1
#                 permutation[l] = i

#                 # 둘 다 level을 인덱스로 사용해야한다. 
#                 # 거시적으로 보았을 때 노드 하나 내려갈 때 맞춰서 곱한 걸 sum에 더한다.
#                 DFS(l+1,sum+permutation[l]*coefficient[l])

#                 check[i] = 0
# if __name__ == "__main__":
#     n,f = map(int, input().split())
#     permutation = [0]*n # 순열 조합 리스트
#     coefficient = [1]*n # 이항 계수 리스트
#     # 이항 계수의 맨 끝은 무조건 1이기 때문에 1로 초기화해준다.
#     check = [0]*(n+1) # 체크 리스트
    
#     # 이항 계수 리스트 값 넣기
#     for i in range(1,n):
#         # 3C0, 3C1, 3C2, 3C3 이 수열의 효과를 나타내기 위함
#         # 파스칼의 삼각형을 생각하자
#         coefficient[i] = coefficient[i-1]*(n-i)//i
#     sum = 0
#     DFS(0,0)

