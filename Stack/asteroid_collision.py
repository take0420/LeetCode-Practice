class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # asteroid が負の数のときのみ衝突の可能性あり
            while stack and asteroid < 0 < stack[-1]:
                # 直前の asteroid が小さい場合は破壊される
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                # asteroid が同じサイズの場合は両方破壊される
                elif stack[-1] == -asteroid:
                    stack.pop()
                # asteroid が破壊されるため
                break
            else:
                # 衝突が起きない場合は追加
                stack.append(asteroid)

        return stack
