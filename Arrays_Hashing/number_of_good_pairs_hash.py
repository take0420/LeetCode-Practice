class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # リスト nums 内の各数字の出現回数を辞書形式でカウントするため
        count = defaultdict(int)
        res = 0
        for num in nums:
            res += count[num]
            count[num] + 1
        return res
