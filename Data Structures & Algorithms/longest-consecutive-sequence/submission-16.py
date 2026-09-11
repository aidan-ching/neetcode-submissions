class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #we only want to start when we find a number that is the lowest/highest in the range
        #convert to set first to check
        s_nums = set(nums)

        longest = 0

        for n in nums:
            if n-1 not in s_nums: #this means we are at the lowest range
                count = 0
                curr = n
                while curr in s_nums:
                    curr += 1
                    count += 1

                longest = max(longest, count)

        return longest
