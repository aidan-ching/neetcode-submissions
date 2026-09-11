class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key is tuple of the chars
        m = defaultdict(list)
        for s in strs:
            counter = [0]*26
            for c in s:
                counter[ord(c)-ord('a')] += 1

            m[tuple(counter)].append(s)

        print(m.values())

        return list(m.values())