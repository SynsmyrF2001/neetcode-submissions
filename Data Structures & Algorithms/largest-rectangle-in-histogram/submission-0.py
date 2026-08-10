class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0 # initialize the maximum area to 0
        stack = []
        for i, height in enumerate(heights): # iterate through the heights
            start = i # initialize the start index to the current index
            while stack and stack[-1][1] > height: # while the stack is not empty and the height of the current bar is less than the height of the bar at the top of the stack
                start, h = stack.pop() # pop the top of the stack
                max_area = max(max_area, h * (i - start)) # update the maximum area
                start = start # update the start index to the previous start index
            stack.append((start, height)) # push the current bar onto the stack

        for i in range(len(stack)):
            max_area = max(max_area, stack[i][1] * (len(heights) - stack[i][0]))

        return max_area # return the maximum area