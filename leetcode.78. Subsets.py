class Solution:
    def subsets(self, nums):
        self.all_sets = []
        temp_list = []

        self.get_all_sets(nums, temp_list, 0)
        return self.all_sets

    def get_all_sets(self, nums, temp_list, start):
        self.all_sets.append(temp_list.copy())
        for i in range(start, len(nums)):
            temp_list.append(nums[i])
            self.get_all_sets(nums, temp_list, i+1)
            temp_list.remove(nums[i])