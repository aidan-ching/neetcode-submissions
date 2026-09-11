class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        if len(s) == 0:
            print("too short!")
            return 0
        letters = set()
        letters.add(s[l])
        m = len(letters)
        while r < len(s):
            m = max(m, len(letters))
            if s[r] not in letters:
                letters.add(s[r])
                r += 1
            elif len(letters) > 0:
                letters.discard(s[l])
                l += 1
            elif len(letters) == 0:
                l += 1
                r += 1

        m = max(m, len(letters))
        return m

            





        