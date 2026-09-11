class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -nums[i] = nums[j] + nums[k]

        #we can sort!
        # place results into a set, set(sorted_arrays())

        nums.sort()
        #don't even need to sort later if we sort it all now!
        res = set()

        for i in range(len(nums)):
            target = -nums[i]
            j, k = i + 1, len(nums)-1

            while j < k:
                sum = nums[j] +nums[k]
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    res.add(tuple((nums[i], nums[j], nums[k])))
                    j += 1

        res = list(res)
        for i in range(len(res)):
            res[i] = list(res[i])

        return res


        