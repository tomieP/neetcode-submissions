class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        max_length = 0
        for num in setNums:
            length = 0
            while num - length in setNums:
                length += 1
            max_length = max(max_length, length)
        return max_length