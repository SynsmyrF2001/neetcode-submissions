class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left  = 0
        max_freq = 0
        char_counts = defaultdict(int)
        max_length = 0

        for right in range(len(s)):
            char_counts[s[right]] += 1
            max_freq = max(max_freq, char_counts[s[right]])

            # Current window length
            window_length = right - left + 1

            #Check if the window is valid
            # If replacements needed > k, skrink the window
            if window_length - max_freq > k:
                char_counts[s[left]] -= 1
                left += 1
            
            # Update max_length with the current valid window size
            max_length = max(max_length, right - left + 1)

        return max_length




        