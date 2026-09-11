class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # first we count t

        valid = defaultdict(int)

        for char in t:
            valid[char] += 1

        # we have two hashmaps for the string s
        # one hashmap only keeps track of the valid letters
        # the other one will keep track of all the letters that we do not need, including extra chars from 
        # the valid hashmap

        #iterate until the valid hashmap is complete, then remove from left until its not valid anymore

        sInvalid = defaultdict(int)
        sValid = defaultdict(int)
        minimum = float('inf')
        ans = ""
        print(valid)
        l,r = 0, 0
        while r < len(s):
            print(sValid)
            while valid == sValid:
                #move from left
                if r-l+1 < minimum:
                    minimum = r-l+1
                    ans = s[l:r]
                if s[l] in sInvalid: #check invalid first
                    sInvalid[s[l]] -= 1
                    if sInvalid[s[l]] == 0:
                        sInvalid.pop(s[l])
                #remove from invalid array first
                elif s[l] in sValid: #then check valid
                    sValid[s[l]] -= 1
                    if sValid[s[l]] == 0:
                        sValid.pop(s[l])
                l += 1
            
            if s[r] in valid and (s[r] not in sValid or sValid[s[r]] < valid[s[r]]):
                #then we can iterate sValid
                sValid[s[r]] += 1
            else:
                #else, we can just place within invalid, since we dont care about this value
                sInvalid[s[r]] += 1

            r += 1

        while valid == sValid:
                #move from left
                if r-l+1 < minimum:
                    minimum = r-l+1
                    ans = s[l:r]
                if s[l] in sInvalid: #check invalid first
                    sInvalid[s[l]] -= 1
                    if sInvalid[s[l]] == 0:
                        sInvalid.pop(s[l])
                #remove from invalid array first
                elif s[l] in sValid: #then check valid
                    sValid[s[l]] -= 1
                    if sValid[s[l]] == 0:
                        sValid.pop(s[l])
                l += 1

        return ans

            
                


        