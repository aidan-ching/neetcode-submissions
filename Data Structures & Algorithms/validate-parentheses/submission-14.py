class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opening = set(['(', '{', '['])
        print(opening)

        for c in s:
            if c in opening:
                print("c in opeining")
                stack.append(c)
            else:
                if not stack:
                    return False
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0