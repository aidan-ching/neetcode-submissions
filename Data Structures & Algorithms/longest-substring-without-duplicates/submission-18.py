class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        #default dict to keep track of current substring length
        # curr length is r-l + 1

        length = 0
        counter = defaultdict(int)

        while r < len(s):
            print(l, r, s[l], s[r], counter)
            if counter[s[r]] > 0:
                counter[s[l]] -= 1
                l += 1
            else:
                counter[s[r]] += 1
                r += 1
                length = max(length, r-l)


            
            



        return length
