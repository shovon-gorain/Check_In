class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize n x n matrix with 0s
        matrix = [[0] * n for _ in range(n)]
        
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 1
        
        while left <= right and top <= bottom:
            # Left → Right
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1
            
            # Top → Bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # Right → Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1
            
            # Bottom → Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        
        return matrix
