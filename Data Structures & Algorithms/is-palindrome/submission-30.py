import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        #we want to convert everything to lowercase and only have alpha
        #lets have a set to check for alphabet

        alpha_set = set(string.ascii_lowercase + string.digits)

        s = s.lower()    

        while l < r:
            print(s[l], s[r], l, r)
            if s[l] not in alpha_set:
                l += 1
            elif s[r] not in alpha_set:
                r -= 1
            elif s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
        