class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # loop through whole thing

        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    #init dfs
                    res += 1
                    queue = []
                    queue.append((i,j))
                    while len(queue) > 0:
                        curr = queue.pop()
                        if curr[0] < 0 or curr[0] >= len(grid) or curr[1] < 0 or curr[1] >= len(grid[curr[0]]) or grid[curr[0]][curr[1]] == '0':
                            continue
                        #mark visited
                        grid[curr[0]][curr[1]] = '0'

                        #populate surroundings
                        queue.append((curr[0]-1, curr[1]))
                        queue.append((curr[0], curr[1]-1))
                        queue.append((curr[0]+1, curr[1]))
                        queue.append((curr[0], curr[1]+1))

        return res


                    
        