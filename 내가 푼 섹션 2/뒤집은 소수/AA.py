import sys, math
sys.stdin = open("input.txt", "rt")

n = int(input())

lst = list(map(int,input().split()))



def isPrime(x):
    for i in range(2,int(math.sqrt(x+1))):
        if x%i==0:
            return False
    return True

def reverse(x):
    st = str(x)
    #문자열 뒤집기 인덱싱, 시발 이거 때문에 파이썬 쓰는 구만, 이거 무조건 외워라 시발 개 사기다.
    reversed_str = st[::-1] # 현타오노 시 발
    return int(reversed_str)


for i in lst:
    num = reverse(i)
    if isPrime(num):
        print(num,end=' ')