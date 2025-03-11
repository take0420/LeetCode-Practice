# Solution 1
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        total = 0
        for num in nums:
            total += num # 現在の合計を更新する
            running_sum.append(total) # 更新した合計をリストに追加する

        return running_sum

# Solution 2
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] # 累積和を直接更新する
        return nums
