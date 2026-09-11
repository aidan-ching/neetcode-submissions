class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def key(s):
            arr = [0] * 26
            for char in s:
                arr[ord(char) - ord('a')] += 1

            return tuple(arr)
        
        hm = defaultdict(list)

        for s in strs:
            hm[key(s)].append(s)

        return hm.values()