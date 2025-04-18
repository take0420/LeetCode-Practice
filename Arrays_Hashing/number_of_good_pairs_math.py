class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0

        for num, c in cnt.items():
            ans += c * (c - 1) // 2

        return ans
