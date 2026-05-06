class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        MAX_SIZE = len(nums)
        my_list = []
        for i in nums:
            my_list.append(i)
        my_list = set(my_list)
        if len(my_list) == MAX_SIZE:
            return False
        else:
            return True
        

        