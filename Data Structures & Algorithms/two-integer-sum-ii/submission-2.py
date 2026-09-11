class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1

        while True:
            total = numbers[l] + numbers[r]
            #if too high we move r down
            if total > target:
                r -= 1
            #if too low we move l up
            elif total < target:
                l += 1
            else:
                return [l+1, r+1]

