class Solution:
    def isPalindrome(self, s: str) -> bool:

        #i think we should clean the stirng first
        #turn to all lower case
        s = s.lower()
        s_cleaned = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                s_cleaned += char
        
        print(s_cleaned)

        l,r = 0, len(s_cleaned)-1


        while l < r:
            print(s_cleaned[l], s_cleaned[r])
            if s_cleaned[l] != s_cleaned[r]: return False
            l += 1
            r -= 1
        return True