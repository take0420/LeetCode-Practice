from typing import List
from collections import defaultdict

def most_frequent_diff(nums: List[int]) -> int:
  """
  与えられた数値配列の隣接する要素間の差の絶対値の中で、
  最も出現頻度が高いものの出現頻度を計算します。

  Args:
    nums: 数値のリスト。

  Returns:
    最も出現頻度が高い差の絶対値の出現頻度。
    配列長が1以下の場合は0を返します。
  """
  # 配列長が1以下の場合、差は計算できないので0を返す
  if len(nums) < 2:
    return 0

  freq_map = defaultdict(int)
  most_freq_diff_cnt = 0 # 最大頻度を記録

  for i in range(len(nums)-1):
    # 隣り合う要素の差の絶対値を計算
    diff = abs(nums[i+1] - nums[i])
    # 差の出現頻度を更新
    freq_map[diff] += 1
    # それまでの最頻値と今の計算で求めた絶対値値を比較し、より大きい方を新たな最頻値とする。
    most_freq_diff_cnt = max(most_freq_diff_cnt, freq_map[diff])

  return most_freq_diff_cnt
