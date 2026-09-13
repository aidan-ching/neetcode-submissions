class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hash map solution

        #nums[i] + nums[j] == target
        # nums[i] == target - nums[j] means we found a solution. Else 

        # 3,4,5,6 #target = 7
        # first loop: is 3 in map, no, enter it into map
        # second loop: 

        map = {}
        for i in range(len(nums)):
            if target - nums[i] in map:
                return [map[target - nums[i]], i]

            map[nums[i]] = i