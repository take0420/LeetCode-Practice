class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        remainder_count = defaultdict(int)
        remainder_count[0] = 1
        total_subarrays = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in remainder_count:
                total_subarrays += remainder_count[remainder]

            remainder_count[remainder] += 1

        return total_subarrays
