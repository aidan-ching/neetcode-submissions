class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #first we have a small loop k to init the first value

        #Hashmap counter -> subtract left pointer
        #keep track of the current maximum
        res = []
        counter = defaultdict(int)
        maximum = float("-inf")
        for i in range(k):
            counter[nums[i]] += 1
            maximum = max(nums[i], maximum)

        res.append(maximum)

        l,r = 0, k-1
        #subwindow is nums[l:r+1]
        while r < len(nums)-1:
            #we have to slide both
            #first lets add the right side
            r += 1
            counter[nums[r]]+=1
            #update maximum if possible
            maximum = max(nums[r], maximum)

            #remove the left pointer from counter
            counter[nums[l]] -= 1
            if counter[nums[l]] == 0:
                #update maximum with subarray
                maximum = max(nums[l+1:r+1])
            l += 1
            res.append(maximum)
        return res

            




        