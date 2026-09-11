class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is string of 26 numbers comma seperated 
        group = defaultdict(list)

        for s in strs:
            #generate key
            #first we count
            key_list = [0] * 26

            for c in s:
                key_list[ord(c) - ord('a')] += 1

            #then we convert it to a comma seperated string

            for i in range(len(key_list)):
                key_list[i] = str(key_list[i])
            key = ",".join(key_list)

            group[key].append(s)

        print(group)

        return list(group.values())
            
