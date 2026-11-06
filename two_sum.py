class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        mydict = {}
        count = 0
        for i in range(len(nums)):
            if target - nums[i] in mydict:
                return [i,mydict[target-nums[i]]]
            else:
                mydict[nums[i]] = i