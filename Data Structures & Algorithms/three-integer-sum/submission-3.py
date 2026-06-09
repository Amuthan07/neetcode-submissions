class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            fixed = i
            left = fixed + 1 or fixed - 1
            right = n - 1
            while left < right:
                tripletSum = nums[fixed] + nums[left] + nums[right]
                if (tripletSum == 0):
                    if ([nums[fixed],nums[left],nums[right]] not in result):
                        result.append([nums[fixed],nums[left],nums[right]])
                        left += 1
                        right -= 1
                    else:
                        left += 1
                        right -= 1
                elif (tripletSum < 0):
                    left += 1
                else:
                    right -= 1
        return result