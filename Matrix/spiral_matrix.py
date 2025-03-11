class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        res = []
        top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
        
        while left < right and top < bottom:
            res.extend(matrix[top][left:right])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            res.extend(matrix[bottom - 1][left:right][::-1])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res
