class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count same as before and use tuple as map key. Return map.values()

        #defaultdict(list)

        m = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            
            m[tuple(count)].append(s)
        return list(m.values())
