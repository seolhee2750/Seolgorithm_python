while True:
    n = input()
    if n == '.': break

    stack = []
    for i in n:
        if i == '.':
            if len(stack) > 0: print("no")
            else: print("yes")
        elif i == '(': stack.append(i)
        elif i == '[': stack.append(i)
        elif i == ')':
            if len(stack) == 0: print("no"); break
            elif stack[-1] == '(': stack.pop(-1)
            else: print("no"); break
        elif i == ']':
            if len(stack) == 0: print("no"); break
            elif stack[-1] == '[': stack.pop(-1)
            else: print("no"); break