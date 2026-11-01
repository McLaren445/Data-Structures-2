def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack  # True if stack is empty
# Test cases
print(is_balanced("()"))  # True
print(is_balanced("([{}])"))  # True
print(is_balanced("(]"))  # False
print(is_balanced("([)]"))  # False
print(is_balanced(""))  # True
print(is_balanced("(()"))  # False
print(is_balanced("a(b)c[d]"))  # True (ignores non-brackets)