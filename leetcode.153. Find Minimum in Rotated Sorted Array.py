class Solution:
    def findMin(self, nums):
        i = 0
        j = len(nums) - 1
        if nums[i] <= nums[j]:
            return nums[i]
        while j - i > 1:
            middle = (i + j) // 2
            if nums[middle] > nums[i]:
                i = middle
            elif nums[middle] < nums[j]:
                j = middle
        return min(nums[i], nums[j])
# 方法二
class Solution:
    def findMin(self, nums):
        i = 0 
        j = len(nums)-1
        while i < j:
            middle = (i + j) // 2
            if nums[middle] < nums[j]:
                j = middle
            else:
                i = middle + 1
        return nums[i]