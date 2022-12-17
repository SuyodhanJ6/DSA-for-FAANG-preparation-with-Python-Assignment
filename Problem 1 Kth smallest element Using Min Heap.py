# Time Complexity : O(nLogN)
import heapq
class Solution:
    def __init__(self):
        pass
    
    def kthSmallestElement(self, nums, k):
        """
        Method Name : kthSmallestElement
        Description : This method help to find the kth smallest element using min heap we are poping 
                        first element then check the condition we are given.
        Output      : int
        On Failure  : None
        """
        # Base Case
        if not nums or len(nums) < k:
            return -1
        # list is converted into min heap
        heapq.heapify(nums)
        
        while k > 1:
            heapq.heappop(nums)
            k -= 1
            
        return nums[0]
    
# Driver Code
arr = [7,2,5,1,3]
k = 2
s = Solution()
print(s.kthSmallestElement(arr,k))