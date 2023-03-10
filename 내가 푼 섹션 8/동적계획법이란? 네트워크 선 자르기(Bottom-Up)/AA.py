import sys
sys.stdin=open("input.txt","r")



# 동적계획법 => Dynamic Programming

# 어떤 문제가 존재하는데 단번에 풀기 어려우면 
# 작은 단위로 직관적으로 줄여서 해결한다.
# 가장 작은 단위에서 값을 구하면 그것을 메모(Memoization)해서 저장한다.
# 이것을 단위를 조금씩 크게해 전 단위에서 구한 값을 이용해서 값을 구하고
# 그것을 저장한다.

# 고등학교 때 배운 수열, 점화식을 생각하자
# 이산수학에서 배웠던 귀납적 추론을 생각하자

# 이 문제를 보자 => 1번은 1, 2번은 2, 3번은 4
# 규칙을 찾아야한다. 등차수열일지 등비수열일지
# 점화식을 떠올리자 f(n) = 2f(n-1)

# 이렇게 n = 1일 때, n = 2일 때 ... n = n + 1 일 때 까지 올라가는 것을 바텀 업(Bottom - Up) 기법이라고 한다.


# dy라는 리스트를 만들고 n(길이)이 = 1 일 때 방법의 수를 기록
# 그 다음 n = 2 일 때 방법의 수와 n = 1일 때 방법의 수를 합쳐서 기록
# 1(n = 1) + 1
# 3 부터 점화식을 알아낸다.

# 길이 3에서 맨 마지막의 길이가 1일 때 전에 구해 놓은 2가 경우의 수가 된다.
# 2(n = 2)
# 그 다음 길이 3에서 마지막의 길이가 2일 때 남은 1이 경우의 수 n = 1일 때 경우의 수가 된다. 
# 1(n = 1)
# => 2 + 1 = 3

# 길이 4에서 맨 마지막의 길이가 1일 때 
# n = 3의 경우의 수가 되므로 3을 가져온다.
# 길이 4에서 맨 마지막의 길이가 2일 때 
# n = 2의 경우의 수가 되므로 2를 가져온다.
# => 3 + 2 = 5

# 길이 5에서 맨 마지막의 길이가 1일 때
# n = 4의 경우의 수가 되므로 5를 가져온다.
# 길이 5에서 맨 마지막의 길이가 2일 때 
# n = 3의 경우의 수가 되므로 3을 가져온다.
# => 5 + 3 = 8

# 길이 6에서 맨 마지막의 길이가 1일 때
# n = 5의 경우의 수가 되므로 8을 가져온다.
# 길이 6에서 맨 마지막의 길이가 2일 때
# n = 4의 경우의 수가 되므로 5를 가져온다.
# => 8 + 5 = 13


# Top - down 기법
# 재귀함수로 구현
# DFS(7)의 경우 DFS(6) + DFS(5)가 되고
# DFS(6)의 경우 DFS(5) + DFS(4)가 되듯이
# 쭉 내려가는 것이다. (전위 순회)
# DFS(2) + DFS(1) 이 될 때까지 내려가면
# 계산을 시작한다.
# 아래에서 올라올 때 기록할 곳을 만들어서
# 메모한다.
# memo = [0]*(n+1)
# 올라갈 때 겹치는 연산이 발생하면
# 메모한 값을 가져온다.
# memo[2]값이 존재하면
# DFS(3)을 돌릴 떄 memo[2]를 가져오면 된다.
# 즉, return memo[n]
# cut edge 
# 메모를 해놓고 불필요한 연산을 제거한다.



def DFS(len):
    if len == 1 or len == 2:
        return len
    
        # edge cut, 메모이제이션을 통한 다이나믹 프로그래밍
    if memo[len] != 0:
        return memo[len]

    else:
        # 메모이제이션
        memo[len] = DFS(len-1) + DFS(len-2)
        return memo[len]

if __name__ == '__main__':

    # 탑 다운 기법

    n = int(input())
    memo = [0] * (n+1)
    print(DFS(n))





    # 바텀 업 기법
    # n = int(input())

    # # 메모할 공간 , 메모이제이션
    # memo = [0] * (n+1)
    # # 1번부터 사용하려고 n+1개
    # # 직관적으로 알 수 있는 것은 초기화를 해주는 것이 좋다.
    # memo[1] = 1
    # memo[2] = 2
    
    # for i in range(3,n+1): 
    #       점화식
    #     memo[i] = memo[i-1] + memo[i-2]

    # print(memo[n])
    
