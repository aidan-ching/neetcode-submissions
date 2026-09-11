class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = defaultdict(int)
        for n in nums:
            s[n] += 1

        for key, value in s.items():
            if value > 1:
                return True

        return False
         