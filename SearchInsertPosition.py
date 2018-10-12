def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target <= nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)
    elif target == nums[-1]:
        return len(nums) -1
    low = 0
    high = len(nums) -1
    
    while low <= high:
        mid = int(low+high) // 2
        if target < nums[mid] and target > nums[mid-1]:
            return mid
        elif target > nums[mid] and target < nums[mid+1]:
            return mid+1
        elif target < nums[mid]:
            high = mid -1
        elif target > nums[mid]:
            low = mid + 1
        else:
            return mid

nums = [1,2,3,6]
target = 5
print(searchInsert(nums, target))