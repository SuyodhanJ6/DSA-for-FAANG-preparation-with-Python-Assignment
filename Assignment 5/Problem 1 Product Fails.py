# Time Complexity  : O(logN) 
# Space Complexity is : O(1)
class Solution:
    def __init__(self):
        pass
    
    def findFirstBadVersion(self, arr):
        """
        Method Name  : findFirstBadVersion
        Description  : This method help to find the square root of number 
                        Bur we are using iterative BS. 
                        So Space Complexity is : O(1) why becz we are not using any extra space(stack internally).
        OutPut       : int
        On Failure   : None
        """
        l, r = 0, len(arr)-1 # l : starting r : ending
        while l < r:
            # T(n/2)
            mid  = l + (r-l) // 2
            if arr[mid] == 1:
                r = mid
            else:
                l = mid+1
        return r
arr = [0,0,0,1,1,1,1,1,1]
s = Solution()
print(s.findFirstBadVersion(arr))