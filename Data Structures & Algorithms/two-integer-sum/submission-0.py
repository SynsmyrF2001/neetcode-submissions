class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force approach: check every possible pair of indicies
        # Hashmap approach: store the numbers and their indicies

        # brute force:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []
        
        # hashmap:
        num_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_map:
                return [num_map[comp], i]
            num_map[num] = i
        # return []