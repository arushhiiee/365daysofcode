class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        x=[[0]*len(A[0]) for i in range(len(A))]
        
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==0:
                    if j==0 and i==0:
                        x[i][j]=1
                    elif j==0:
                        x[i][j]=x[i-1][j]
                    elif i==0:
                        x[i][j]=x[i][j-1]
                    else:
                        x[i][j]=x[i-1][j]+x[i][j-1]
        #print(x)
        return x[len(A)-1][len(A[0])-1]
                    
                    

