class Solution {
    public int findMin(int[] nums) {
        // Binary Search Pattern: Sinve the array was sorted prior to rotation, at least one half of the array around the midpoint is always strictly sorted
        // Pivot Identification: The min element is the only element whose predecessor is greater than itself, or the start of the unrotated portion
        /* Comparison Anchor: Compare nums[mid] with nums[right]: 
            -> If nums[mid] > nums[right], the min must liek strictly in the right half (left = mid + 1) b/c the inflection point occurs after mid
            -> If nums[mid] <= nums[right], the right half os sorted, meaning the minimum lies at mid or to its left (right = mid) */
        //  Termination: When left == right. the search space converges to the min element
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return nums[left];
    }
}
