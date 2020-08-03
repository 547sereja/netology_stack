from mystack import Stack


def checking(list):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(list) and balanced:
        symbol = list[index]
        if symbol == '(' or symbol == '[' or symbol == '{':
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                stack.pop()
        index = index + 1
    if balanced and stack.isEmpty():
        return True
    else:
        return False


if __name__ == "__main__":
    print(checking('(((([{}]))))'))
    print(checking('[([])((([[[]]])))]{()}'))
    print(checking('{{[()]}}'))
    print(checking('}{}'))
    print(checking('{{[(])]}}'))
    print(checking('[[{())}]'))
