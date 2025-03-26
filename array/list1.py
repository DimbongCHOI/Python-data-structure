
arr = ["카리나", "윈터", "닝닝", "지젤"]

def Myappend(a):
    arr.append(a)

def Mypop():
    if len(arr) == 0:
        return "리스트가 비었습니다 !" # 예외처리 - 비어버린 리스트에 대해서
    x = arr[len(arr) - 1]
    del arr[len(arr) - 1]
    return x

def Myindex(a):
    for i in range(0, len(arr), 1):
        if arr[i] == a:
            return i
    return -1 # 예외처리 - 없는 값에 대해서

def Myinsert(a, b):
    if a > len(a) - 1:
        return -1 # 예외처리 - 넘어가버린 index 값에 대해서
    for i in range(len(arr) - 1, a, -1):
        arr[i] = arr[i-1] # 0 0  ->  0 none 0

    arr[a] = b

def Myremove(a):
    num = Myindex(a)
    print("찾은 인덱스:", num) # 인덱스 값 확인
    if num == -1: # 예외처리 - 없는 값에 대해서
        return "해당 값이 없습니다"

    arr[num] = None
    for i in range(num + 1, len(arr)):
       arr[i-1] = arr[i]
       arr[i] = None # 마지막으로 None 보내기

    del arr[len(arr) - 1] # 마지막에 있는 none 지우기

#def Mylen()

#def Myreverse():

#def Mycount():
