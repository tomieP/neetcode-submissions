class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i, num in enumerate(nums):
            h[num] = i
        for i,num in enumerate(nums):
            curr = target - num
            if curr in h and h[curr] != i:
                return [i,h[curr]]
