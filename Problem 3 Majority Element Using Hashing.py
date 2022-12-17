# Time Complexity  : O(n)
# Space Complexity : O(n)
from collections import Counter
class Solution:
    def __init__(self):
        pass
    def printMajorityElements(self, nums):
        count = Counter(nums)
        print(count)
        return max(count.keys(), key = count.get)

# Driver Code
nums = [1,2,4,3,2, 2, 2]
s = Solution()
print(s.printMajorityElements(nums))