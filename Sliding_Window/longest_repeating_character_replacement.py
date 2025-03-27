class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}        # ウィンドウ内の各文字の出現回数を保持する辞書
        left = 0          # ウィンドウの左端
        max_freq = 0      # 現在のウィンドウ内で最も多く出現している文字の数
        result = 0        # 求める最長部分文字列の長さ

        # 右側のポインタでウィンドウを右に広げながら探索
        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            max_freq = max(max_freq, count[char])
            
            # ウィンドウサイズから最頻出文字の数を引いた値が k より大きい場合は縮小
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result
