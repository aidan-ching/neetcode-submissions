class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # add up left and right
        # if sum is larger than target, move right down
        # if sum is lower than target, move left up

        l,r = 0, len(numbers)-1

        while l<r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l+1, r+1]