import sys
sys.stdin = open("input.txt", "rt")


n , m = map(int,input().split())

lst = list(map(int,input().split()))

# # 이거 내림차순으로 바꾸는 거
# lst.sort(reverse=True)

lst.sort()

print(lst)

s = 0
e = len(lst) - 1

while s<=e:
    middle = (s+e)//2
    if lst[middle] < m:
        print(lst[middle])
        s = middle + 1
    elif lst[middle] > m:
        print(lst[middle])
        e = middle - 1
    else:
        break

# 몇 번째냐고 했으니까 ㅋㅋ 시발 플러스 1 해줘라
print(middle+1)
print()
print(s+1)
print()
print(e+1)


