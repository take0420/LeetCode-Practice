class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index, t_index = 0, 0
        s_length, t_length = len(s), len(t)

        while s_index < s_length and t_index < t_length:
            if s[s_index] == t[t_index]:
                s_index += 1  # 一致したらsの次の文字に進む
            t_index += 1  # 毎回tの次の文字に進む
        
        return s_index == s_length  # sを最後まで確認できたかチェック
