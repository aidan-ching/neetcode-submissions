class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # lets convert to set first of all.
        # we dont run the loop to check for longest conseq if the number isn't on the top of the range
        # say its 7 we check if 8 is in the set. Only if its the largest number we can check if there are things smaller

        n_set = set(nums)

        longest = 0

        for n in n_set:
            count = 1

            if n+1 not in n_set:
                # this is when we keep checking as n is the largest in the sequence
                curr = n-1
                while curr in n_set:
                    curr -= 1
                    count += 1
                
                longest = max(longest, count)


        return longest
        