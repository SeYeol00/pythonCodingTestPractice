import sys
sys.stdin = open("input.txt", "rt")


# 그리디 알고리즘
# 정렬하고 순서 보고 정리하는 습관이 중요하다.
n = int(input())

storage = list(map(int,input().split()))

m = int(input())

storage.sort(reverse=True)

print(storage)


# 한 번 소팅하고 다시 소팅하자 
# 횟수로만 할 거면 언더바 쓰자
for _ in range(m):
    storage[0] = storage[0] - 1
    storage[n-1] = storage[n-1] + 1
    storage.sort(reverse=True)
print(storage)


print(max(storage)-min(storage))