class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums[i] + nums[j] = target
        #nums[j] = target - nums[i]

        map = {}
        for i in range(len(nums)):
            if target-nums[i] in map:
                return [map[target-nums[i]], i]
            else:
                map[nums[i]] = i
                