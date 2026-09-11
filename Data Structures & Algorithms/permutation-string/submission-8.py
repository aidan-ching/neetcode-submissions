class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm1 = defaultdict(int)
        hm2 = defaultdict(int)

        if len(s1) > len(s2):
            return False

        #count s1 first
        for char in s1:
            hm1[char] += 1

        #we count s2 using the length of s1

        #first we fill out the second dict with the initial values

        for i in range(len(s1)):
            hm2[s2[i]] += 1

        # print(hm2)


        l,r = 0, len(s1)-1

        while r < len(s2)-1:
            if hm1 == hm2:
                # print(hm1,hm2, s2[l:r])
                return True
            else:
                # print(hm1, hm2, s2[l:r])
                hm2[s2[l]] -= 1
                if hm2[s2[l]] == 0:
                    hm2.pop(s2[l])
                r += 1
                l += 1
                # print(s2[r])
                hm2[s2[r]] += 1

        if hm1 == hm2:
            # print(hm1,hm2, s2[l:r])
            return True

        return False


        
        