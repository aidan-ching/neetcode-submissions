class Solution:
    def isValid(self, s: str) -> bool:
        map = {"(" : ")", "{" : "}", "[" : "]"}

        stack = []

        for char in s:
            if char in map:
                stack.append(char)

            elif len(stack) > 0 and char == map[stack[-1]]:
                stack.pop()
            else:
                return False

        return True if len(stack) == 0 else False