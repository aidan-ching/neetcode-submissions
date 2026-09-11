class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = set(['[', '{', '('])
        for c in s:
            if c in open:
                stack.append(c)
            elif len(stack) == 0 or (len(stack) > 0 and (c == ']' and stack[-1] != '[') or (c == '}' and stack[-1] != '{') or (c == ')' and stack[-1] != '(')):
                return False
            else:
                stack.pop()

        return len(stack) == 0
                
        