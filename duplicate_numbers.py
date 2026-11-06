class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_nos = set()

        for i in nums:
            if i not in unique_nos:
                unique_nos.add(i)
            else:
                return True
        return False
    

"""

optimal solution



class Solution(object):
    def containsDuplicate(self, nums):
        my_set = set(nums)
       
        if len(my_set) == len(nums):
            return False
            
        else:
            return True
            
        
"""