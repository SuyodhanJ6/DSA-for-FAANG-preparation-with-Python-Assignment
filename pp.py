import sys

# Partition the nums and return the index of pivot
def partition(nums, l, h):
    x = nums[h]
    i = l
    for j in range(l, h):
	# Swapping smaller elements to the left side of the pivot
        if (nums[j] <= x):
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            
    nums[i], nums[l] = nums[l], nums[i]
    return i

def kthSmallest(nums, l, h, k):
    if (k > 0 and k <= h - l + 1):
        # Partition the nums array and get the index of pivot
        index_of_pivot = partition(nums, l, h)

        if (index_of_pivot - l == k - 1): #Kth smallest element is at index_of_pivot
            return nums[index_of_pivot]
        if (index_of_pivot - l > k - 1): # Process the left side
            return kthSmallest(nums, l, index_of_pivot - 1, k)
        # Else Process right side
        return kthSmallest(nums, index_of_pivot + 1, h,k - index_of_pivot + l - 1)

    return sys.maxsize

# Initializing the nums, k, and n
nums = [40, 25, 68, 79, 52]
k = 4
n = len(nums)

print(k,"th smallest element is:", kthSmallest(nums, 0, n - 1, k))