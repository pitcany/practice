#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maxElement = float("-inf")

    def Push(self, a):
        if a <= self.maxElement:
            self.__stack.append(a)
        else:
            if self.__stack == []:
                self.__stack.append(a)
            else:
                self.__stack.append(2*a-self.maxElement)
            self.maxElement = a

    def Pop(self):
        assert(len(self.__stack))
        popped=self.__stack.pop()
        if popped > self.maxElement:
            self.maxElement = 2*self.maxElement - popped

    def Max(self):
        assert(len(self.__stack))
        return self.maxElement


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
