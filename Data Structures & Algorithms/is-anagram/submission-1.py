class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use hashmap to store the freq. of each character in the first string
        # iterate through the second string and decrement the count of each character in the hashmap
        # If at any point the count of a character becomes negative or if the strings have different lengths, they cannot be anagrams
        # after iterating through the second string check if all the counts in the hashmap are zero
        # If they are then the strings are anagrams
        # If the lengths of the strings are different at the start return false early

        # Most optimized
        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)

        # Under the hood w/ Hashmap
        if len(s) != len(t):
            return False
        
        char_counts = {}

        for char in s: 
            char_counts[char] = char_counts.get(char, 0) + 1
        
        for char in t:
            if char not in char_counts:
                return False
            char_counts[char] -= 1
            if char_counts[char] < 0:
                return False
        return True



        