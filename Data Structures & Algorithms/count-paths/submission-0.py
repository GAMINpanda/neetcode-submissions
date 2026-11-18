class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # store solutions from an index
        # use adjacent indexes to find variations from current point

        num_solutions = [[0] * n for _ in range(m)]

        # back track from end, going left and up

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                #print("i:", i)
                #print("j:", j)
                right_val = 0
                bottom_val = 0

                statement1 = (i != m-1)
                statement2 = (j != n-1)
                if statement1:
                    bottom_val = num_solutions[i + 1][j]
                if statement2:
                    right_val = num_solutions[i][j + 1]

                if not statement1 and not statement2:
                    num_solutions[i][j] = 1
                else:
                    num_solutions[i][j] = right_val + bottom_val

                #print ("bottom_val:", bottom_val)
                #print ("right_val:", right_val)
        
        return num_solutions[0][0]

