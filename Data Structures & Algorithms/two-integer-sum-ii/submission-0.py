class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l<r:
            total = numbers[l]+numbers[r]
            
            #if too little, we move l += 1
            #if too much we move right down
            if total < target:
                l += 1
            elif total  > target:
                r -=1
            else:
                return [l+1,r+1]
        