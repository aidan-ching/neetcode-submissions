class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #have a hashmap with the key being the value and the value being the index where it is at

        mp = {}

        for i,n in enumerate(nums):
            print(mp)
            if target-n in mp:
                return [mp[target-n], i]
            else:
                mp[n] = i

        


        