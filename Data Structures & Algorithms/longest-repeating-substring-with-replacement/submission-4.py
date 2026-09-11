class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #so we can count how many letters are in the substring.
        #keep track of the maximum letters using a variable
        #hashmap to keep track of the current count of letters
        #maybe we dont need a hashmap and a set together
        #set to keep track of what letters are inside the hashmap

        l,r = 0, 0 
        hm = defaultdict(int)
        #so our maximum will be our value that is not replaced, and the rest is len(substring) - maximum
        #this len(substring) - maximum cannot exceed k
        maxLetter = ""
        maximumLetters = 0
        maxLength = 0
        #check for max Length every time we run the loop
        while r < len(s):
            #length is r-l+1
            hm[s[r]] += 1
            print(hm, maximumLetters, maxLetter)

            #check if its that letter or need to be replaced
            if hm[s[r]] >= maximumLetters:
                maxLetter = s[r]
                maximumLetters = hm[s[r]]
            #here we check if its still a valid substring

            while (r-l+1) - maximumLetters > k:
                hm[s[l]] -= 1
                if s[l] == maxLetter:
                    maximumLetters -= 1
                l += 1

            maxLength = max(maxLength, r-l+1)
            r += 1

        return maxLength


        





        