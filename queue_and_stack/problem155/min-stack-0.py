import math


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minStack.append(min(x, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> float:
        return self.minStack[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()
