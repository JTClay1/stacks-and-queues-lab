def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """

    # using a list as a stack
    # opening brackets get pushed on
    # then popped off when matching closing brackets show up
    stack = []

    # each closing bracket should match the opener shown here
    matches = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    # go through the string one character at a time
    for char in s:

        # if it's an opening bracket, push it onto the stack
        if char in matches.values():
            stack.append(char)

        # if it's a closing bracket, it needs to match the most recent opener
        elif char in matches:

            # if stack is empty, there's nothing to match with
            if not stack:
                return False

            # grab the most recent opening bracket
            top = stack.pop()

            # if the opener doesn't match the current closer, it's invalid
            if top != matches[char]:
                return False

    # valid only if there are no unmatched opening brackets left
    return len(stack) == 0