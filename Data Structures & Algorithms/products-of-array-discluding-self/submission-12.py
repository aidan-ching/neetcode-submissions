class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # [1,2,4,6]

        #[48, 24, 12, 8]

        # 48 = 1 * (2*4*6) the left side
        # 24 = (1) * (4*6)
        # 12 = (1*2) * (6)
        # 8 = (1*2*4) * (1)
        
        #[1,1,2,8] pre
        #[48,24,6,1] post

        # 2 arrays length of the thing all 1s
        pre, post, res = [], [], []

        count_pre = 1
        count_post = 1
        for i in range(1, len(nums)+1):
            pre.append(count_pre)
            count_pre *= nums[i-1]
            post.insert(0,count_post)
            count_post *= nums[-i]

        for i in range(len(nums)):
            res.append(pre[i]*post[i])
        

        print(pre)
        print(post)

        return res



