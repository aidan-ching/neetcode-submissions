import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert all to lower
        s = s.lower()

        accepted = set(string.ascii_lowercase).union(set(string.digits))

        l,r = 0, len(s)-1

        while l < r:
            while s[l] not in accepted and l < r:
                l += 1
            while s[r] not in accepted and l < r:
                r -= 1

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True