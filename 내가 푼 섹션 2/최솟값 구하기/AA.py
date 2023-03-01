
arr=[5,3,7,9,2,5,2,6]

#float('inf')는 파이썬의 최댓값을 뜻한다.
#arrMin = float('inf')

min = arr[0]


for i in range(len(arr)):
    if min > arr[i]:
        min = arr[i]

print(min)