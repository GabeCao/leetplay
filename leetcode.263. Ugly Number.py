class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        while num % 2 == 0:
            num = num // 2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5
        return True if num == 1 else False

sl = Solution()
print(sl.isUgly(7))
# if num <= 0:
#             return False
#
#         for i in [2, 3, 5]:
#             while num%i == 0:
#                 num = num / i
#         return True if num == 1 else False