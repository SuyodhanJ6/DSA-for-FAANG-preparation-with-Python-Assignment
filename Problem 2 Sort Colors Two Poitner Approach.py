class Solution:
    def __init__(self):
        pass
    
    def sortColors(self, nums):
        """
        Method Name  : sortColors
        Description  : This is two pointer approach by  Dijkstra himself --> https://en.wikipedia.org/wiki/Dutch_national_flag_problem
        Output       : list
        On Failure   : None
        """
        white, red , blue = 0,0,len(nums)-1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        return nums
# Driver Code
nums = [2,0,2,1,1,0]
s = Solution()
print(s.sortColors(nums))