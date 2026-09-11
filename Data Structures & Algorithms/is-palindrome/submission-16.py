import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #run through the string with two pointers
        accepted = set(string.ascii_lowercase) | set(string.digits)
        s = s.lower()
        l, r = 0, len(s)-1

        while l < r:
            while l<r and s[l] not in accepted:
                l += 1
            while l<r and s[r] not in accepted:
                r -= 1

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

        