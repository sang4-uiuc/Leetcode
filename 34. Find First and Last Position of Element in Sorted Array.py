class Solution:
    # double binary search method
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if len(nums) == 0:
            return -1, -1
        left, right = -1, -1
        l, r = 0, n-1
        while l < r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
                print(l)
            else: r = m
        if nums[l] != target:
            return -1, -1
        left = l
        l, r = left, n-1
        while l < r:
            m = (l+r)//2+1
            if nums[m] == target: l = m
            else: r = m-1
        right = l
        return left, right

    # smarter method where the index returns the index of the first target
    # and reversing the list can get you the index of the last target
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        if target not in nums:
            return([-1,-1])
        res.append(nums.index(target))
        res.append(len(nums)-nums[::-1].index(target)-1)
        return(res)
        