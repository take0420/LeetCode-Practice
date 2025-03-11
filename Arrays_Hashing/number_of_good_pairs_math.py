class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # リスト nums 内の各数字の出現回数を辞書形式でカウントするため
        count = Counter(nums)
        res = 0

        for num, c in count.items():
            res += c * (c - 1) // 2
        return res
