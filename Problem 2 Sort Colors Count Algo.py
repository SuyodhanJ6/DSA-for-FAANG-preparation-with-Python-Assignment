class Solution:
    def __init__(self):
        pass
    
    def sortColors(self, nums):
        """
        Method Name  : sortColors
        Description  : This is brut force approach 
        Output       : list
        On Failure   : None
        """
        c1, c2, c3 = 0, 0, 0
        for i in nums:
            if i == 0:
                c1 += 1
            elif i == 1:
                c2 += 1
            else:
                c3 += 1
        nums[:c1] = [0] * c1
        nums[c1:c1] = [1] * c2
        nums[c1+c2:] = [2] * c3
        return nums
        
        
# Driver Code
nums = [2,0,2,1,1,0]
s = Solution()
print(s.sortColors(nums))