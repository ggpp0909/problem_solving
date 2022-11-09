# stack 이라는 자료구조
class Stack:
    # stack -> 처음 주어지는 길이 만큼
    def __init__(self, arr):
        self.arr = arr
        self.top = -1

    # append를 직접 구현하자
    # stack에 추가할 n
    def push(self, n):
        # 어디에?
        self.top += 1
        self.arr[self.top] = n

    # pop
    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.arr[self.top + 1]
        else:
            raise IndexError('list out of range')

    # 비어 있는지 체크
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    # 현재 top에 있는 원소
    def peek(self):
        return self.arr[self.top]

m = 5
stack = Stack([0]*m)
print(stack.arr)
print(stack.top)
print('='*30)
stack.push(3)
print(stack.arr)
print(stack.top)
print(stack.peek())
print('='*30)
print(stack.pop())
print(stack.arr)
print(stack.top)
print(stack.is_empty())
print('='*30)
stack.push(0)
print(stack.arr)
print(stack.top)
print(stack.is_empty())
stack.push(1)
stack.push(2)
print(stack.arr)
print(stack.top)
stack.push(3)
stack.push(4)
print(stack.top)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
