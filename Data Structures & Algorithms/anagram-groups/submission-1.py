class Solution:
    def getCode(self, s):
        x = [0] * 26
        print(ord("z") - ord("a"))
        for char in s:
            x[ord("z") - ord(char)] += 1

        return tuple(x)



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for s in strs:
            sol[self.getCode(s)].append(s)
        return sol.values()
        