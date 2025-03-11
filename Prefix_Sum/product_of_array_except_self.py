class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # 左からの累積積（prefix product）
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]

        # 右からの累積積（suffix product）
        suffix_prod = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix_prod *= nums[i + 1]
            res[i] *= suffix_prod

        return res
