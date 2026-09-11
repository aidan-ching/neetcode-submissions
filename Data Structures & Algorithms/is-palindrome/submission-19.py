class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        while l<r:
            # validate left and right
            if not s[l].isalpha() and not s[l].isdigit():
                l += 1
                continue
            if not s[r].isalpha() and not s[r].isdigit():
                r -= 1
                continue
            #check if left and right are the same
            if not s[l].lower() == s[r].lower():
                return False

            l += 1
            r -= 1

        return True
