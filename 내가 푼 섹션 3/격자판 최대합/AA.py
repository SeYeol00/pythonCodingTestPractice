import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

a = []

for _ in range(n):
    lst = list(map(int, input().split()))
    a.append(lst)

largest = 0

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):  # 원리 생각하기
        sum1 += a[i][j] # 행렬, i행의 합
        sum2 += a[j][i] # 행렬, i열의 합
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1+= a[i][i]
    sum2 += a[i][n-i-1]

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
print(largest)

