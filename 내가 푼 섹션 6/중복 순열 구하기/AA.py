import sys
sys.stdin=open("input.txt","r")


# 부분집합은 이진트리로 DFS를 사용하여 판별했지만
# 중복 순열(중복을 허락하여 n번 뽑아 나열한다.)은 여러 가닥으로 dfs가 뻗어 나간다.
# dfs(0) -> dfs(1), dfs(2),dfs(3) 세 가닥으로 뻗어야한다.
# res라는 리스트를 생성해서 i를 인덱스로 받아서 내려갈 값을 넣어준다.


def DFS(l):
    global cnt # 글로벌 선언

    if l==m: # 하나의 중복 순열 완성 level이 끝에 다다를 때
        for i in res:
            print(i,end=" ")
        print()
        cnt+=1
    else:
        for i in range(1,n+1): # 1부터 3까지
            res[l] = i # l레벨에서 1을 넣을건가 2를 넣을 건가 3을 넣을건가
            DFS(l+1)


if __name__ == "__main__":
    n,m = map(int, input().split())
    res=[0]*m # m의 크기를 가진 중복순열을 담을 리스트
    cnt = 0
    DFS(0)
    print(cnt)




# class Test:
#     name=""
#     number=0

#     def __init__(self, name, number):
#         self.name = name
#         self.number = numberß

#     def hello(self):
#         print(self.name)
#         print(self.number)


# if __name__ == "__main__":
#     print("hello world")
#     t = Test("seyeolpark",25)
#     t.hello()
