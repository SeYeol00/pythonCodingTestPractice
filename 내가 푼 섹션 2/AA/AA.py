import sys
sys.stdin = open("input.txt", "rt")


#파이썬에서는 map이 인풋으로 쓰인다.
n, k = map(int, input().split(" "))

count = 0

#1부터 n까지 돌아라 
for i in range(1,n+1):
    if n%i ==0:
        count += 1
    if count == k:
        print(i)
        break
else:
    print(-1)
    

