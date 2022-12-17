"""
Time Complexity  : O(n)
Space Complexity : o(1)

Boyer Moore Voting Alog.
"""
class Solution:
    def __init__(self):
        pass
    def findCandidate(self, nums):
        """
        Method Name : findCandidate
        Description : Helps to find the majority element in the array. using boyer moore voting.
        Output      : int
        On Failure  : None
        """
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
            # count == (1 if candidate == num else -1)
        return candidate
    
    def isMajority(self, nums, candidate):
        size = len(nums)
        count = 0
        for i in range(size):
            if nums[i] == candidate:
                count += 1
        if count > size/2:  # condition
            return 1
        else:
            return 0
            
    
    def printMajorityElements(self, nums):
        candidate = self.findCandidate(nums)
        if self.isMajority(nums, candidate):
            print(f"The majority number is : {candidate}")
        else:
            print("There is no majority is present")

# Driver Code
nums = [3,2,3,4,3]
s = Solution()
s.printMajorityElements(nums)