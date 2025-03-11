class Solution:
  def maxScore(self, s: str) -> int:
    n = len(s)
    left_zeros = 0
    right_ones = s.count('1') # 全体の'1'の数をカウントする
    max_score = 0 # 最大スコアを保持する変数をセットする

    for i in range(n-1): # 最後の要素は分割できないため
      if s[i] == '0':
        left_zeros += 1
      else:
        right_ones -= 1

      max_score = max(max_score, left_zeros + right_ones) # 最大スコアを更新する

    return max_score
