import sys
import itertools as it
sys.stdin=open("input.txt","r")

# 이 문제는 결국 부분집합을 만들어서 검증하는 것이다.
# 주어진 n개의 숫자 중에 m개의 숫자를 뽑아서 사용하는 것이다.
# 그 m개의 원소들의 합을 받아서 6의 배수인지 판별하면 된다.

# a라는 리스트를 크기 n으로 만들어서 다 저장해두고 그 값을 인덱싱 하여
# 넣어보자
# sum + a[i] 이렇게 누적해서 넘긴다.
# i는 S에 for문을 돌리면서 하면 된다.


# 방법 2

n,k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0


# 조합은 combinations()
for x in it.combinations(a,k):
    if sum(x) % m == 0:
        cnt += 1

print(cnt)









# 방법 1

# def DFS(L,S,sum):
#     global cnt
#     if L==k:
#         if sum%m == 0:
#             cnt +=1
#     else: # 자료가 리스트에 들어가 있는데 이 인덱스를 받아야한다.
#         # 처음에는 a[0]부터 a[n-1]까지 돌아야하고
#         # 이후 시작점을 S를 받아서
#         # 돌아야한다.
#         for i in  range(S,n):
#             # i+1를 넘겨야한다. 인덱스를 넘긴다.
#             # 지금 넣은 
#             DFS(L+1,i+1,sum+a[i])

# if __name__ == "__main__":
#     n,k=map(int, input().split())
#     a = list(map(int, input().split()))
#     m=int(input())
#     cnt=0
#     DFS(0,0,0)
#     print(cnt)

     