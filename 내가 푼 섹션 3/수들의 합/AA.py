import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

a = list(map(int, input().split()))


#범위는 투 포인터 법칙으로 푼다.
lt = 0
rt = 1
total = a[0]
count = 0

# 그림을 그리면서 포인터 두 개를 전진시켜보자
while True:
    if total < m:
        if rt < n:
            total +=a[rt]
            rt+=1 # rt 전진 시키기
        else:
            break #인덱스가 넘어가니 브레이크
    elif total == m:
        count+=1
        total-=a[lt]
        lt+=1
    else:
        total-=a[lt]
        lt+=1
    
print(count)