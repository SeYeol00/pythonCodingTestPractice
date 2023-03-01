import sys, math
sys.stdin = open("input.txt", "rt")


n = int(input())

# 체크리스트를 만들어야한다. 범위는 n+1로 왜냐면 저거 인덱싱으로 푸는 거임
lst = [0]*(n+1)

count = 0
for i in range(2,int(math.sqrt(n)+1)):
    for j in range(i+1,n+1): # i 뒤에서 시작한다. 
        if(j%i==0):
            lst[j]+=1 # 나누어 지면 체크

for i in range(2,len(lst)):
    if lst[i]==0:
        print(i,end=" ")