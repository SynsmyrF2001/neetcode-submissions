class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key = lambda x: x[0], reverse = True) # sort the cars by position in descending order
        stack = []
        for pos, speed in cars:
            stack.append((target -  pos) / speed) # calculate the time it takes for the car to reach the destination
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # if the current car catches up to the car in front of it, then it is part of the same fleet
                stack.pop()
        return len(stack) # return the number of car fleets
        