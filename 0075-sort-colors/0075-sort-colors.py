class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        last_zero = 0   
        first_two = len(nums) - 1
        any_one = 0

        while any_one <= first_two:
            if nums[any_one] == 0:
                nums[last_zero], nums[any_one] = nums[any_one], nums[last_zero]
                any_one += 1
                last_zero += 1
            elif nums[any_one] == 1:
                any_one += 1
            else:
                nums[first_two], nums[any_one] = nums[any_one], nums[first_two]
                first_two -= 1