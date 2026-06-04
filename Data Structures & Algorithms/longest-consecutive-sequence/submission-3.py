class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = set(nums)
        result = 0
        for num in freq:
            if num-1 not in freq:
                length = 1
                while num+length  in freq:
                    length+=1
                result = max(length,result)
        return result
        