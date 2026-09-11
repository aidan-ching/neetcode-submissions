import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        accepted = set(string.ascii_lowercase) | set(string.digits)

        s= s.lower()

        l, r = 0, len(s)-1

        while l < r:
            while l < len(s) and s[l] not in accepted:
                l += 1
            while r >= 0 and s[r] not in accepted:
                r -= 1

            # print(s[l], s[r], l, r)
            if l < len(s) and r >= 0 and s[l] != s[r]:
                return False
            
            l += 1
            r -= 1

        return True



        