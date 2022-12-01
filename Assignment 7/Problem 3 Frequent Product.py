class Solution:
    def __init__(self):
        pass
    
    def frequentProduct(self, list):
        """
        Method Name  : collinearOrNot
        Description  : This method help to find the product
                        purchased most frequently.
        OutPut       : string
        On Failure   : None
                        
        """
        # Create Dictionary
        dict = {}
        for i in list:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        maximum = max(dict, key = dict.get)
        return maximum  
                
                
        # Approach 2 using Counter Method
        """
        from collections import Counter
        dict = dict(Counter(list))
        dict.sort()  # Time Complexity : O(nLogN)
        max = 0
        for i in dict:
            if max < dict[i]:
                max = dict[i] # We Found max value in the dict
        re_list = []
        for key, value in dict:
            if max == value:
                re_list.append(key)
        return re_list[-1] """
        
        
        
# Driver Code
# list = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt',
# 'greenPants', 'greenPants', 'greenPants']

list = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt']
s = Solution()
print(s.frequentProduct(list))