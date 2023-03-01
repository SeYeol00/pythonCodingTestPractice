# 퀵정렬

# 병합 정렬은 선위 순회 방식
# 퀵정렬은 후위 순회 방식

# 병합 정렬은 먼저 나누고 그 다음 정렬
# 퀵정렬은 정렬하고 나눔

# 파티션 => 중심 값을 가지고 왼쪽과 오른쪽을 나눈다. == 분할

# 즉 병합정렬 => 선 파티션, 후 정렬
# 퀵정렬 => 선 정렬, 후 파티션

# 퀵정렬 또한 병합정렬과 같이 분할해서 생각한다.

# 퀵정렬은 피벗값을 지정해야한다. 피벗을 결정하는 데에 있어 성능 차이가 난다.
# 요새는 맨 오른쪽 값을 가장 많이 쓴다.
# 피벗값 == 중심값
# 피벗 값을 정하고 파티션을 진행
# pivot = arr[rt]


def QSort(lt, rt):
    if lt < rt:
        # lt 부터 rt 전까지, 왼쪽이 오른쪽보다 크다면 정지다.
        pos = lt # pos 정하기, pos는 인덱스다.
        pivot = arr[rt] # pivot 정하기, pivot은 값이다.

        for i in range(lt,rt):
            # pivot 값과 arr[i]를 비교해서
            # 정렬을 시작한다. pivot 값이 arr[i]보다 크면
            # arr[pos]와 arr[i]의 값을 스왑
            # 스왑이 진행됐다면 pos에 1을 더해 인덱스를 증가시킨다.
            # pivot 값과 arr[i]를 다시 비교한다.
            if arr[i] <= pivot:
                temp = arr[i]
                arr[i] = arr[pos]
                arr[pos] = temp
                pos+=1
        
        # for문이 끝나면 arr[pos]와 pivot의 값을 스왑한다.
        temp = arr[pos]
        arr[pos] = pivot
        arr[rt] = temp
        
        # 이 다음에 분할! 재귀를 쓰자
        # DFS => 상태트리, 분할정렬은 => 분할 단계
        # pos는 가운데 기준이므로 포함하지 말자
        # 이미 기준을 세워서 나눴기 때문이다.
        QSort(lt, pos - 1)
        QSort(pos+1, rt)

        
            

if __name__ == "__main__":
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print("Befoe sort : ", end = '')
    print(arr)
    # 처음 인덱스 부터 끝 인덱스까지 정렬
    QSort(0, len(arr)-1)
    print("After sort : ", end = '')
    print(arr)