import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int,input().split())

lst = []

for _ in range(n):
    lst.append(int(input()))


# print(lst)

# 결정 알고리즘에서 이분 탐색을 사용한다.
# 결정 알고리즘 -> 최댓값과 1을 잡고 이분 탐색 하기
# 들어오는 최댓값과 1로 시작해서 중간값으로 나눈 몫들의 합을 비교한다.

start = 1
last = max(lst) # 이게 더 낫다 이걸 쓰자 이건 n 밖에 안 걸림
# min max 활용 잘하자 파이썬은 이런 거 ㅈㄴ 많다.

while start <= last:
    # 미드 포인트 잡고
    middle = (start + last)//2
    
    # 먼저 갯수를 셉시다.
    num = 0
    for i in lst:
        left = i//middle
        num+=left

    # 갯수로 판별해서 미들을 옮기자
    if num < m:
        last = middle - 1
    elif num > m:
        start = middle + 1
    else:
        break


print(middle)
