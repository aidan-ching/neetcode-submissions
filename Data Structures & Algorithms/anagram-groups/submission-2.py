class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #lets have a map, where the key is a tuple 0,0,0 of alphabet count
        mp = defaultdict(list)

        for s in strs:
            mp[self.countLetters(s)].append(s)

        return mp.values()

    def countLetters(self, s: str) -> tuple:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        return tuple(count)
        