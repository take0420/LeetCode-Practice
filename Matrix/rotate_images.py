class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        left, right = 0, n - 1  # 行列の境界（外側のレイヤーから内側へ進める）

        while left < right:
            for i in range(right - left):  # 各層の回転処理（上端を基準に進める）
                top, bottom = left, right
                
                # 一時変数に左上の値を保存
                topLeft = matrix[top][left + i]

                # 左下 → 左上
                matrix[top][left + i] = matrix[bottom - i][left]

                # 右下 → 左下
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # 右上 → 右下
                matrix[bottom][right - i] = matrix[top + i][right]

                # 保存していた左上 → 右上
                matrix[top + i][right] = topLeft

            # 内側の層へ移動
            left += 1
            right -= 1