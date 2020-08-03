class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __repr__(self):
        return f"The object stack {self.stack}"


if __name__ == '__main__':
    first = Stack()
    print(first.isEmpty())
    first.push(12345)
    first.push(56789)
    first.push([00000])
    print(first)
    print(first.peek())
