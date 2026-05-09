class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = sorted(nums)
        freq = {}
        for num in nums:
            if num in freq: freq[num] += 1
            else: freq[num] = 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, f in freq.items():
            bucket[f].append(num)
        result = []
        for f in range(len(nums), 0 , -1):
            for num in bucket[f]:
                result.append(num)
                if len(result) == k:
                    return result