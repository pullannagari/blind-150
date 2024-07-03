class Solution:
    def twoSum(self, nums: 'list[int]', target: int) -> 'list[int]':
        if len(nums) < 2:
            return None
        target_map = {}
        for index, num in enumerate(nums):
            if num in target_map:
                return [target_map[num], index]
            else:
                target_map[target-num] = index
        
        