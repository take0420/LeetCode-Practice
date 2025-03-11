class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total_sum = 0

        for i in range(n):
            total_sum += mat[i][i]
            total_sum += mat[i][n-i-1]

        # 行列のサイズが奇数ならば、中央の要素が二重加算されているため調整する
        if n % 2 == 1:
            total_sum -= mat[n//2][n//2]

        return total_sum
