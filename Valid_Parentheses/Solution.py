class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            '(': ')',
            '[': ']',
            '{': '}'}

        for bracket in s:
            if bracket in closeToOpen.values():
                if not stack or stack.pop() != bracket:
                    return False
            else:
                stack.append(closeToOpen[bracket])

        return len(stack) == 0
        