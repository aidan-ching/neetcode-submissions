class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0

        l,r  = 0, 0
        maxf = 0

        while r < len(s):
            count[s[r]] += 1

            maxf = max(maxf, count[s[r]]) # max freqeuncy of whatever we've seen
            # print(r-l+1, maxf, s[r])
            print(s[l:r+1])

            while (r-l+1) - maxf > k:
                print(s[l:r+1])
                # print(r-l+1, maxf, s[r])

                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1

        return res






        