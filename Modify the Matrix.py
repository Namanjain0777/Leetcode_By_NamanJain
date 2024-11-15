class Solution:
    def modifiedMatrix(self, matrix) :
        r=len(matrix)
        c=len(matrix[0])
        for i in range (r):
            for j in range (c):
                if matrix[i][j]==-1:
                    max1=0
                    for p in range (r):
                        max1=max(max1,matrix[p][j])
                    matrix[i][j]=max1
        return matrix
        
