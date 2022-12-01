from asyncore import close_all


class Solution:
    def __init__(self):
        pass
    
    def closetSum(self, arr, target):
        """
        Method Name  : closetSum
        Description  : This method help to find the sum of three int to the target.
        OutPut       : int
        On Failure   : None
                        
        """
        
        closetSum = abs(target*100000)
        arr.sort()

        for i in range(len(arr) - 2):
            left = i+1
            right = len(arr)-1
            
            sumOfValue = arr[i] + arr[left] + arr[right]
            if abs(target - sumOfValue) < abs(target - closetSum):
                closetSum = sumOfValue
            
            elif sumOfValue > target:
                right -= 1
            else:
                left += 1   
                
        return closetSum
    
        """
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result
        """
    
# Driver Code
arr = [0,1,2]
target = 0
s = Solution()
print(s.closetSum(arr, target))