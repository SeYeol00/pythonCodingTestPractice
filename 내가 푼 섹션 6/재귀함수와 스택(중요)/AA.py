# 재귀함수와 스택
import sys
sys.stdin=open("input.txt","r")

# 재귀함수는 반복문의 대체
# 코드가 유연성있게 작성 가능하다.
# 재귀함수는 스택으로 구현되어 있다.
# 그렇기 때문에 DFS를 구현할 때 재귀함수를 사용하는 것이다.
# 스택이라는 메모리 영역이 생성된다.
# 메모리에 함수에 대한 매개변수를 다 기록해둔다.
# 지역변수도 메모리에 할당이 된다.
# 복귀 주소라는 것이 존재한다. DFS(x)에 대한 특별한 주소가 있다.
# 이렇게 매개변수, 지역변수, 복귀 주소 세개가 한 덩어리로 묶여서 함수로 작동 중이다.
# 이 한 덩어리를 스택 프레임이라한다. 메모리에 저장하는 하나의 단위가 된다.

def DFS(x):
    if x == 0:
        return
    print(x,end='')
    return DFS(x-1)





if __name__ == "__main__":
    n = int(input())
    DFS(n)