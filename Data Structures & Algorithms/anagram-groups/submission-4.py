class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        hm = defaultdict(list)

        for s in strs:
            hm[self.generateKey(s)].append(s)

        return hm.values()


    def generateKey(self, s):
        #key will be a tuple of 26 chars

        key = [0] * 26

        for char in s:
            key[ord(char) - ord('a')] += 1

        return tuple(key)