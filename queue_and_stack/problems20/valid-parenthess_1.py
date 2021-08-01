def isValid(s: str):
    if len(s) % 2 == 1:
        return False
    pairs = {')': "(",
             '}': '{',
             ']': '['}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or pairs[ch] != stack[-1]:
                return False
            else:
                stack.pop()
        else:
            stack.append(ch)
    return not stack
