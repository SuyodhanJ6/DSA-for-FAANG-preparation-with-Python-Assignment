# Time Complexity  : O(logN) 
# Space Complexity is : O(1)
class Solution:
    def __init__(self):
        pass
    
    def isValidPerfectSquare(self, num):
        """
        Method Name  : isValidPerfectSquare
        Description  : This method help to find the perfect square root of number 
                        Bur we are using iterative BS. 
                        So Space Complexity is : O(1) why becz we are not using any extra space(stack internally).
        OutPut       : boolean
        On Failure   : None
        """
        l, r = 0, num
        while l <= r:
            # T(n/2)
            mid = l + (r-l) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1 
        return False
# Driver Code
num = 16
s = Solution()
print(s.isValidPerfectSquare(num))