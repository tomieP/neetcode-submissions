class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        max_length = 0
        for num in setNums:
            if num - 1 not in setNums:
                curr_num = num
                length = 1
                while curr_num + 1 in setNums:
                    curr_num += 1
                    length += 1
                max_length = max(length, max_length)
        return max_length