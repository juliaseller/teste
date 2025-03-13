def busca_binaria(nums, target):
    left = 0
    right = len(nums) - 1
    
    mid = (left+right)//2

    while left <= right:
        mid_val = nums[mid]
        if mid_val == target:
            return mid_val
        
        if target > mid_val:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1 
