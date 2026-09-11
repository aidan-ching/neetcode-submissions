class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #count each string and return if same
        countOne = defaultdict(int)

        countTwo = defaultdict(int)

        for char in s:
            countOne[char] += 1

        for char in t:
            countTwo[char] += 1

        return countOne == countTwo
