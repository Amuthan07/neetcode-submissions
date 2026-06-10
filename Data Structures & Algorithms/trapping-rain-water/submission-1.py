class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) 
        left_max = []
        max_left = height[0]
        right_max = [0] * n
        max_right = height[-1]
        total_water = 0

        for i in range(n):
            max_left = max(max_left, height[i])
            left_max.append(max_left)
        
        for i in range(n-1,-1,-1):
            max_right = max(max_right, height[i])
            right_max[i] = max_right

        for i in range(n):
            water_at_i = min(left_max[i], right_max[i]) - height[i]
            total_water += water_at_i

        return total_water