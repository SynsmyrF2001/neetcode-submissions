class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            # Calculate current area
            # width = r - l
            height = min(heights[l], heights[r]) * (r - l)
            max_water = max(max_water, height)

            # Move pointer at shorter bar
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water

        '''
        Strategy

        1. Start wide: place pointer at the leftmost bar (index 0) and one at the rightmost bar (index n - 1)
        2. Calculate area: width right(r) - left(l), height = min(height[left(l)], height[right(r)])
        3. Move shorter side: If the left bar is shorter, move left pointer; otherwise move right pointer left
        4. Keep track of maximum: Update the max area after each calculation
        '''
        