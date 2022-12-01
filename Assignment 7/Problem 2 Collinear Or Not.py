import math
class Solution:
    def __init__(self):
        pass
    
    def collinearOrNot(self, x1, y1, x2, y2, x3, y3):
        """
        Method Name  : collinearOrNot
        Description  : This method help to find the pt are collinear or not.
                        collinear means all pt are in one line 
                        1. using slope 
                        2. using area of triangle
                        3. using distance formula
        OutPut       : string
        On Failure   : None
                        
        """
        if math.sqrt(((x2-x1)**2 + (y2-y1)**2)) + math.sqrt(((x3-x2)**2 + (y3-y2)**2)) == math.sqrt((x3-x1)**2 + (y3-y1)**2):
            print("YES")
        else:
            print("NO")
            
# Driver Code
x1, y1, x2, y2, x3, y3 = 1,1, 1,6, 0,9#1,1, 1,4, 1,5
s = Solution()
print(s.collinearOrNot(x1, y1, x2, y2, x3, y3))
