class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()

        #set to keep track of the letters in the substring

        l,r = 0, 0

        maximum = 0

        while r < len(s):

            while s[r] in letters:
                letters.remove(s[l])
                l += 1

            letters.add(s[r])
            maximum = max(maximum, len(letters))

            r += 1

        return maximum

            
        