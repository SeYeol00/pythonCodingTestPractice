import sys
sys.stdin = open("input.txt", "rt")


n, k = map(int, input().split())

Array = list(map(int, input().split()))

#중복을 제거하는 자료구조 => set 중요
res = set()
# 셋은 순서가 없으므로 리스트화 해서 소팅을 돌려야한다

#브루트포스
for i in range(n):
    # i 바로 뒤부터 돌아라
    for j in range(i+1,n):
        # j 바로 뒤부터 돌아라
        for m in range(j+1,n):
            res.add(Array[i]+Array[j]+Array[m])

list = list(res)

#내림차순 정렬
list.sort(reverse=True)
print(list[k-1])
