class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums2 = sorted(nums)
        res = []

        for i, n in enumerate(nums2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if n + nums2[left] + nums2[right] == 0:
                    if [n, nums2[left], nums2[right]] not in res:
                        res.append([n, nums2[left], nums2[right]])
                    left += 1
                if n + nums2[left] + nums2[right] < 0:
                    left += 1
                if n + nums2[left] + nums2[right] > 0:
                    right += -1
            left = i + 1
            right = len(nums) - 1
        return res