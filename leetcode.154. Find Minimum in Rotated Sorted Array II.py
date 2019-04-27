class Solution:
    def findMin(self, nums):
        i = 0
        j = len(nums) - 1
        while i < j:
            middle = (i + j) // 2
            if nums[middle] < nums[j]:
                j = middle
            elif nums[middle] > nums[j]:
                i = middle + 1
            else:
                j -= 1
        return nums[i]
