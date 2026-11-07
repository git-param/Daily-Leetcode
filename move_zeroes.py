class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) in [0,1]:
            return

        # nums_copy = nums[:]
        # mydict = {
        #     'zero_ele': [],
        #     'non_zero_ele': []
        # }
        # for index in range(len(nums)):
        #     if nums[index] == 0:
        #         mydict['zero_ele'].append(index)
        #     else:
        #         mydict['non_zero_ele'].append(index)

        # count= 0
        # for i in mydict['non_zero_ele']:
        #     nums[count] = nums_copy[i]
        #     count += 1

        # for i in mydict['zero_ele']:
        #     nums[count] = nums_copy[i]
        #     count += 1
        
        current = 0
        next_non_zero_index = 0

        while current < len(nums):
            if nums[current] != 0:
                nums[next_non_zero_index] = nums[current]
                if next_non_zero_index != current:
                    nums[current] = 0
                next_non_zero_index += 1
            current += 1