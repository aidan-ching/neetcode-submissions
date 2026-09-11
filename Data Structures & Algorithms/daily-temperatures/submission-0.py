class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i,temp in enumerate(temperatures):
            j = i+1
            while j < len(temperatures) and temperatures[j] <= temp:
                j += 1
            res.append(j-i if j < len(temperatures) else 0)

        return res
            

        