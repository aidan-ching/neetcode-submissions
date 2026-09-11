import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ACCEPTED = list(string.ascii_lowercase) + list(string.digits)

        l,r = 0, len(s)-1

        s = s.lower()

        while l<r:
            while s[l] not in ACCEPTED:
                l+=1
                if l>=r:
                    return True
            
            while s[r] not in ACCEPTED:
                r-=1
                if l>=r:
                    return True

            print(s[l],s[r])

            if s[l] != s[r]:
                return False

            else:
                l+=1
                r-=1
        
        return True
            
