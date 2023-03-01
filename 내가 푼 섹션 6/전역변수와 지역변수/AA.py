# 전역 변수와 지역 변수



def DFS():
    a[0] = 7
    print(a)


def DFS1():
    cnt=3
    print(cnt)

def DFS2():
    global cnt
    if cnt == 5:
        cnt+=1
        print(cnt)

if __name__ == '__main__':
    cnt=5
    a = [1,2,3]
    DFS()
    DFS1()
    DFS2()
    print(cnt)