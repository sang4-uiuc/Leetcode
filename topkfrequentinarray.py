# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


import collections

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    
    output = []
    c = collections.Counter(nums)
    res = c.most_common(k)
    print(res)
    for i in res:
        output.append(i[0])
    return output
arr = [1,1,1,2,2,3]
k = 2
print(topKFrequent(arr, k))