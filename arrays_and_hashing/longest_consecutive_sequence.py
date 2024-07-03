class Solution:
    def longestConsecutive(self, nums: 'list[int]') -> int:
        num_set = set(nums)
        con_count = 0
        result = 0
        for num in nums:
            con_count = 0
            while num in num_set:
                con_count += 1
                num -= 1
            if con_count > result:
                result = con_count
        
        return result