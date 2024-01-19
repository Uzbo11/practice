class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] != 1:
                return nums[i] + 1
        if 0 not in nums:
            return 0
        else:
            return len(nums)