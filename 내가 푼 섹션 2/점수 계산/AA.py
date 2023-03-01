import sys, math
sys.stdin = open("input.txt", "rt")

n = int(input())

lst = list(map(int,input().split()))

answer = [0]*(n)
count = 0
for i in range(len(lst)):
    if lst[i] == 0:
        answer[i] = 0
        count = 0
    elif lst[i] == 1:
        if count == 0:
            answer[i]+=1
            count+=1
        else:
            answer[i]+=(1+count)
            count+=1
print(answer)