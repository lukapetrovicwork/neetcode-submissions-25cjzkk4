class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #for i in range(len(nums)):
        #    left_sum = sum(nums[:i])
        #    right_sum = sum(nums[i+1:])
        #    if left_sum == right_sum:
        #        return i
        #return -1

        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left += nums[i]

        return -1