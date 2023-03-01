import sys
sys.stdin = open("input.txt", "rt")

n = int(input())


candidates = []

for _ in range(n):
    can = tuple(map(int,input().split()))
    candidates.append(can)

# 키로 한 번 이미 정렬함
# 즉 키로 한 번 거르고 몸무게까지 지면 안 센다 이런 느낌
candidates.sort(reverse = True, key= lambda x :x[0])

print(candidates)

compare = candidates[0] # 맨 앞
cnt = 1 # 이미 맨 앞은 통과가 되었기 때문

for i in range(1,n):
    if candidates[i][1] >= compare[1]:
        cnt+=1
    compare = candidates[i]

print(cnt)
