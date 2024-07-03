class Solution:
    def productExceptSelf(self, nums: 'list[int]') ->'list[int]':
        l_p = [1]*len(nums)
        r_p = [1]*len(nums)

        for i in range(1, len(nums)):
            l_p[i] = nums[i-1]*l_p[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            r_p[j] = nums[j+1]*r_p[j+1]
        
        result = []
        for i in range(len(nums)):
            result.append(l_p[i]*r_p[i])
        
        return result

