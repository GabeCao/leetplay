class Solution:
    def nthUglyNumber(self, n):
        if n < 7:
            return n
        nums = [1 for _ in range(n)]
        x = 0
        y = 0
        z = 0
        for i in range(1, n):
            nums[i] = min(min(nums[x] * 2, nums[y] * 3), nums[z] * 5)
            if nums[i] == nums[x] * 2:
                x += 1
            if nums[i] == nums[y] * 3:
                y += 1
            if nums[i] == nums[z] * 5:
                z += 1
        return nums[n-1]

sl = Solution()
print(sl.nthUglyNumber(10))