class Solution:
    def count(self, s):
        solution = defaultdict(int);
        for char in s:
            solution[char] += 1

        return solution
    
    def isAnagram(self, s: str, t: str) -> bool:
        return (self.count(s) == self.count(t))
        