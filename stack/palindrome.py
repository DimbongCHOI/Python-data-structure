# check - palindrome
class Stack:
    def __init__(self, size): # 선언 시, size는 최대 크기를 받아옴
        if not isinstance(size, int):
            raise TypeError("size는 정수여야 합니다.")
        if(size <= 0): # (2) 0보다 커야함
            raise ValueError("입력 시, size는 0보다 큰 정수여야 합니다.")
        self.stack = [None] * size # None으로 채워진 size 크기의 리스트 생성
        self.top = -1 # 스택이 비었음 == -1 (맨 위의 인덱스)
        self.FULL = size # 최대 크기인 size로 FULL을 초기화 (추후, 함수에 사용) FULL == len(self.stack)

    def printStack(self): # 출력 함수
        print("스택:", self.stack[:self.top+1]) # 0 ~ top 까지 슬라이싱 출력 (들어있는 모든 값 출력)

    def isStackFull(self): # 스택 다 찼음? 함수
        return self.top + 1 == self.FULL # top은 index 값이므로 개수보다 1 적으므로 +1 값과 FULL 비교

    def isStackEmpty(self): # 스택 비어있음? 함수
        return self.top == -1 # -1 이면 비어버린 스택. 아무 것도 존재하지 않음 -> pop에서 Error처리? ok

    def push(self, data): # 위에 쌓기 함수
        if(self.isStackFull()): # 다 찼으면 더 이상 쌓으면 안 됨
            print("Stack is full!")
            return
        self.top += 1 # 초기 값 -1이라 먼저 ++
        self.stack[self.top] = data # top 인덱스에 data 넣어주기

    def pop(self): # 위에서 빼기 함수
        if(self.isStackEmpty()): # 비었으면 더 이상 빼면 안 됨
            print("Stack is empty!")
            return None # data 돌려주는 대신 None를 드립니다
        data = self.stack[self.top] # 삭제되는 데이터 알려주려 리턴하기 위해 저장
        self.stack[self.top] = None # None 으로 죽여버리기, 아예 없어지는 건 아님
        self.top -= 1 # top 인덱스 값 - 1 .. 1층 낮아짐
        return data # data 궁금하면 봐 ㅋ

def isPalindrome(val): # ver1 : Quiz - G : 앞 뒤로 읽어도 같은 값
        pal = Stack(len(val) // 2)
        isTrue = True
        i = 0

        if(len(val) // 2 == len(val) / 2): # 짝수
            for _ in range(len(val) // 2):
                pal.push(val[i])
                i += 1
                # pal.printStack()
            for _ in range(len(val) // 2):
                n = pal.pop()
                # print("pop값", n)
                # print("val값", val[i])
                if(n == val[i]):
                    isTrue = True
                    i += 1
                else:
                    isTrue = False
                    break
        else: # 홀수
            for _ in range(len(val) // 2):
                pal.push(val[i])
                i += 1
                # pal.printStack()
            for _ in range(len(val) // 2):
                n = pal.pop()
                # print("pop값", n)
                # print("val값", val[i])
                if(n == val[i + 1]):
                    isTrue = True
                    i += 1
                else:
                    isTrue = False
                    break

        return isTrue

val = input("판별할 값 입력: ")
result = isPalindrome(val)
print(result)
