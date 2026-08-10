class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        n = len(height)

        # Build max_left: tallest bar from left up to postiton i
        max_left = [0] * n
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])
        
        # Build max_right: tallest bar from left up to position i
        max_right = [0] * n
        max_right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
        
        # Calculate total trapped water
        total = 0
        for i in range(n):
            water_level = min(max_left[i], max_right[i])
            total += water_level - height[i]
        
        return total