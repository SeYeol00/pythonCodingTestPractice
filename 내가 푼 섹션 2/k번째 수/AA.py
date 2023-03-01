import sys
sys.stdin = open("input.txt", "rt")

#2
T = int(input())

# 2번 실행한다.
for i in range(T):
    n,s,e,k = map(int,input().split())
    
    A = list(map(int,input().split()))
    
    # 인덱스 슬라이싱
    a=A[s-1:e] # s번째부터 e번째까지
    
    # 퀵 소트 리스트 소팅 
    a.sort()
    # f스트링 기억하자
    print(f"#{i+1} {a[k-1]}")

