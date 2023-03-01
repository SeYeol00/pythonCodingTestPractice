import sys
sys.stdin = open("input.txt", "rt")

n,m = map(int,input().split())

# 파이썬의 리스트 갯수 지정 방식
# 외우기
# 파이썬은 리스트를 더하고 뺄 수 있다. ㄷㄷ
cnt = [0]*(n+m+1) # 핵심

max =0 # 항상 임의의 비교수는 맥스는 0, 민은 아주 큰 수 이렇게 하자
# 매트릭스 만들기, 행렬 만들기
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1

# print(cnt)

#최댓값을 먼저 찾자
for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]

#최댓값을 이용하여 인덱스를 서치하자
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ') # 옆으로 출력하는 방법