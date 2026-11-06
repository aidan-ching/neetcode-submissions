class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a key of the string
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        # subtract char with ord('a'), compare the array if its the same then we are good.
        for char in s:
            s_dict[char] += 1
        for char in t:
            t_dict[char] += 1

        return s_dict == t_dict
