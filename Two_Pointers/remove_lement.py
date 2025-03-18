class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 書き込み位置を示す pointer を初期化する
        write_index = 0

        for read_index in range(len(nums)):
            # 現在の要素が val と異なる場合、書き込み位置に格納する
            if nums[read_index] != val:
                nums[write_index] = nums[read_index]
                write_index += 1  # 書き込み位置を一つ進める

        # val 以外の要素の数を返す
        return write_index
