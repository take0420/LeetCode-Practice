class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        # 各回転パターンが有効かを保持するリスト
        # インデックスの意味:
        # 0: 90° clockwise, 1: 180°, 2: 270°, 3: 0°(no rotation)
        valid_rotations = [True, True, True, True]

        for i in range(n):
            for j in range(n):
                # 0°の比較
                if valid_rotations[3] and mat[i][j] != target[i][j]:
                    valid_rotations[3] = False
                # 90°の比較
                if valid_rotations[0] and mat[i][j] != target[j][n-i-1]:
                    valid_rotations[0] = False
                # 180°の比較
                if valid_rotations[1] and mat[i][j] != target[n-i-1][n-j-1]:
                    valid_rotations[1] = False
                # 270°の比較
                if valid_rotations[2] and mat[i][j] != target[n-j-1][i]:
                    valid_rotations[2] = False
                
            # 処理の途中で全ての回転が不一致ならば早期終了
            if not any(valid_rotations):
                return False
        
        return any(valid_rotations)
