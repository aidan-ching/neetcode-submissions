class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        maxLen = 0
        curr = set()

        while r < len(s):
            if s[r] not in curr:
                curr.add(s[r])
                maxLen = max(maxLen, len(curr))
                r += 1
            else:
                # if its a dupe
                while s[r] in curr:
                    curr.discard(s[l])
                    l += 1

        return maxLen
        

        