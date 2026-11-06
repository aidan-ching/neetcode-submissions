class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create map
        # loop through strs
            #create a key (tuple val of )
            #insert key into map

        #return map.values()

        m = {}
        for s in strs:
            key = [0]*26
            for char in s:
                key[ord(char) - ord('a')] += 1
            l_item = m.get(tuple(key), [])
            l_item.append(s)
            m[tuple(key)] = l_item

        return list(m.values())
