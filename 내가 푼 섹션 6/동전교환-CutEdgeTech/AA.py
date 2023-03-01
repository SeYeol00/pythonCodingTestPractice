import sys
sys.stdin=open("input.txt","r")



# DFS는 결국 판별에 몇 개의 가지로 뻗어 나가는지에 대한 문제다.
def DFS(l,sum):
    global res

    # 실패, 우리가 가진 답보다 레벨이 큰 것은 자동으로 가지를 쳐야한다.
    if l>res:
        return

    # 실패, sum이 n보다 크면 결국 안 된다.
    if sum> m: # 변수 잘 봅시다 ㅜㅜ
        return
    
    # 성공 
    if sum==m:
        # 최소 조건 필요
        if res>l:
            res = l
        
    else:
        for i in range(n):
            DFS(l+1,sum+lst[i])



if __name__ == "__main__":
    n = int(input())
    lst = list(map(int,input())) # 리스트는 글로벌 선언 필요없다 주소 참조라
    m = int(input())
    # 주어진 조건에 내림차순 정렬을 해버려야 시간이 오래 걸리지 않고 큰 수부터 넣기 떄문에 금방 된다.
    # 최소 횟수를 원하기 때문이다. 그럼 큰 숫자를 더해야 빨라진다.
    lst.sort(reverse=True)
    # 정답
    res = 13# 최대 동전 갯수를 넘도록 설정
    sum = 0
    DFS(0,sum)
    print(res)