# Time Complexity  : O(logN) 
# Space Complexity is : O(1)
class Solution:
    def __init__(self):
        pass
    
    def squareRoot(self, x):
        """
        Method Name  : squareRoot
        Description  : This method help to find the square root of number 
                        Bur we are using iterative BS. 
                        So Space Complexity is : O(1) why becz we are not using any extra space(stack internally).
        OutPut       : int
        On Failure   : None
        """
        l, r = 0, x # l : starting r : ending
        while l <= r:
            # T(n/2)
            mid = l + (r-l) // 2 # mid value
            if mid * mid <= x < (mid+1) * (mid+1):  #imp
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
        
# Driver Code
x = 10
s = Solution()
print(s.squareRoot(x))