def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    stack = []

    matches = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in matches.values():
            stack.append(char)
        elif char in matches:
            if not stack:
                return False

            top = stack.pop()

            if top != matches[char]:
                return False

    return len(stack) == 0