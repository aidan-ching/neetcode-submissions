class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for i in range(len(matrix)):
            res += matrix[i]

        l,r = 0, len(res)

        while l < r:
            mid = l + (r-l)//2

            if res[mid] >= target:
                if res[mid] == target:
                    return True
                r = mid
            else:
                l = mid+1
        return False

        
        