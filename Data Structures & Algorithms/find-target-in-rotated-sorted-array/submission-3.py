class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute Force approach
        # 1. Iterate through the array and check each element
        # Time: O(n)
        # Space: O(1)

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
        
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            # 1. Direct hit check
            if nums[mid] == target:
                return mid

            # 2. Check if the LEFT half is sorted
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1  # Target is in left half
                else:
                    lo = mid + 1  # Target is in right half

            # 3. Otherwise, the RIGHT half is sorted
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1  # Target is in right half
                else:
                    hi = mid - 1  # Target is in left half

        return -1
