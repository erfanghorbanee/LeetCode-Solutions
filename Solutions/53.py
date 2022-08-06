class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sub = nums[0]
        sum = 0
        
        for n in nums:
            if sum < 0:
                sum = 0
            
            sum+= n
            max_sub = max(max_sub, sum)
        
        return max_sub
