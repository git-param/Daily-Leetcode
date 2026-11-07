class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [None for _ in range(len(nums))]
        left = 0
        right = len(nums) - 1
        position = len(nums) - 1
        
        for _ in range(len(nums)):
            if (nums[left] ** 2) < (nums[right] ** 2):
                result[position] = nums[right] ** 2
                right -= 1
            else:
                result[position] = nums[left] ** 2
                left += 1
            position -= 1
        
        return result