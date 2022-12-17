# Time Complexity  : O(n)
# Space Complexity : O(logN) we calling recursively means we are using stack in backend.
import sys
class Solution:
    def __init__(self):
        pass
    def partition(self, nums, p, q):
        """
        Method Name : partition
        Description : This method help to find the mid element index.
        Output      : int
        On Failure  : None
        """
        pivot = nums[p]
        i = p
        for j in range(i+1, q+1):
            if nums[j] <= nums[i]:
                i +=1
                nums[i], nums[j] = nums[j], nums[i]
                
        nums[i], nums[p] = nums[p], nums[i]
        return i
            
    def kthSmallestElement(self, nums, k, p, q):
        """
        Method Name : kthSmallestElement
        Description : This method help to find the kth smallest element using quick select means we are using 
                        quick sort but using little trick.
        Output      : int
        On Failure  : None
        """
        if (k > 0) and (k <= q - p + 1):
            # Dividing
            mid = self.partition(nums, p, q)
            
            # mid == k
            if mid - p == k -1:
                return nums[mid]
            
            # Lift Side
            if k - 1 < mid-1:
                return self.kthSmallestElement(nums, k , p, mid-1) # mid is perfect number
            return self.kthSmallestElement(nums, k - mid+ p+ 1 , mid+1, q)
        
        return sys.maxsize
        
        # return nums
# Driver Code
nums = [40, 25, 68, 79, 52]

p = 0
q = len(nums)-1
k = 2
s = Solution()
print(s.kthSmallestElement(nums,k, p, q))