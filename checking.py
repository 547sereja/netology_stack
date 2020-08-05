from mystack import Stack


def compare(open, close):
    open_signs = '([{'
    close_signs = ')]}'
    return open_signs.index(open) == close_signs.index(close)


def checking(list):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(list) and balanced:
        symbol = list[index]
        if symbol in '([{':
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                top = stack.pop()
                if not compare(top, symbol):
                    balanced = False

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
