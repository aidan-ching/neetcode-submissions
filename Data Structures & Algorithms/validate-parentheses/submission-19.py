class Solution:
    def isValid(self, s: str) -> bool:
        #stack the opening ones
        # pop when we get the closing ones
        # if they dont match then we have to return false

        pairings = {")" : "(", "]": "[", "}": "{"}

        stack = []

        for char in s:
            if char not in pairings:
                stack.append(char)
            else:
                if len(stack) == 0 or stack.pop() != pairings[char]:
                    return False

        return True if len(stack) == 0 else False