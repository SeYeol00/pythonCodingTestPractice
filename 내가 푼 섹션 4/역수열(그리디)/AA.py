import sys
sys.stdin = open("input.txt", "rt")



# 그리디 -> 정렬된 자료!!! 중요!!!
# 살펴볼 때 정렬된 자료를 쓴다는 것을 명심하자.
# 유념해야되는 것은 자기 차례의 숫자의 앞에 몇 개의 숫자가 존재하는지다.
# 이미 앞에 몇개인지 같은 숫자가 나왔으면 지나치고 넣어야한다.
# 이미 들어간 숫자는 현재 차례의 숫자보다 작은 숫자라는 것을 명심하자

n = int(input())
# a는 역수열
a = list(map(int, input().split()))

# 0번부터 n - 1 인덱스까지만 사용한다는 것을 명심하자.
seq = [0]*n

# a의 인덱스 번호
for i in range(n):
    # seq의 빈 자리를 찾아가는 번호
    for j in range(n):
        if a[i] == 0 and seq[j]==0:
            seq[j] = i+1
            # j를 break, j가 자기 자리를 찾아갔다.
            break
        elif seq[j] == 0:
            a[i]-=1     
              
for x in seq:
    print(x,end=" ")