import sys
sys.stdin=open("input.txt","r")


# 이분 탐색의 연장선
# 병합정렬, 왼쪽 인덱스와 오른쪽 인덱스
# 어레이1과 어레이2가 끊임없이 비교하는 거다.
def Dsort(lt,rt):
    if lt < rt:
        # 중간 값 찾기
        mid = (lt + rt)//2

        # 두 갈래로 뻗어 나누어진다.
        Dsort(lt,mid)
        Dsort(mid,rt)
# ========================== 여기까지 분할, 이 아래는 정복
#       이게 가능한 이유는 리스트의 콜 바이 레퍼런스 때문이다.


        # merge
        # 본연의 일 코딩 
        # - 여기가 merge 코드다.
        
        # 2분할한 왼쪽 자식
        p1 = lt

        # 2분할한 오른쪽 자식
        p2 = mid + 1

        # 임시 리스트 생성
        temp = []

        # 자식들이 한 바퀴 돌 때까지
        # 어느 한 쪽이 다 돌면 멈춰야한다.
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                temp.append(arr[p1])
                p1+=1
            elif arr[p1] > arr[p2]:
                temp.append(arr[p2])
                p2+=1
        
        # p1이 남았다.
        if p1<=mid: # 남은 것들 다 넣자 mid 포함
            temp = temp + arr[p1:mid+1]
        # p2 남았다.
        if p2<=lt: # 남은 것들 다 넣자 lt 포함
            temp = temp + arr[p2:lt+1]
        # 정렬된 temp를 넘겨주어야한다.
        for i in range(len(temp)):
            # 조심 그냥 i에 넣어버리면 0으로 들어간다.
            # lt에 i를 더한 인덱스를 넣어주자
            # 다시 arr에 복사
            arr[lt + i] = temp[i]
        

        # p1이 남았다.

        # p1이 남았다.

    






if __name__ == "__main__":
    arr = [23,11,45,36,15,67,33,21]
    print("Before sort : ", end = "")
    print(arr)
    Dsort(0,7)
    print()
    print("After sort : ", end = "")
    print(arr)