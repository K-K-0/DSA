class Solution:

    # def markrow(self,matrix,n,m,i):
    #         for j in range(m):
    #             if matrix[i][j] != 0:
    #                 matrix[i][j] = -99
    # def markcol(self,matrix,n,m,j):
    #         for i in range(n):
    #             if matrix[i][j] != 0:
    #                 matrix[i][j] = -99


    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])

        row = [0] * n
        col = [0] * m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        return matrix


        # n = len(matrix)
        # m = len(matrix[0])

        
      
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == 0:
        #             self.markrow(matrix,n,m,i)
        #             self.markcol(matrix,n,m,j) 

        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == -99:
        #             matrix[i][j] = 0
        
        # return matrix