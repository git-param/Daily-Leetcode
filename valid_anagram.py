class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        str_dict = {}
        for i in s:
            if i not in str_dict:
                str_dict[i] = 1
            else:
                str_dict[i] += 1
        
        for i in t:
            if i in str_dict:
                if str_dict[i] == 1:
                    str_dict.pop(i)
                else:
                    str_dict[i] -= 1
            else:
                return False
        
        return not str_dict