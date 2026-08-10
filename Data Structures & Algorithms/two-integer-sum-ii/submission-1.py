class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(numbers):
            if target - num in mp:
                return [mp[target - num] + 1, i + 1]
            mp[num] = i
        return []
