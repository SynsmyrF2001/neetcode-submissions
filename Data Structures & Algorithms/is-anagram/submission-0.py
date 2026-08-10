class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use hashmap to store the freq. of each character in the first string
        # iterate through the second string and decrement the count of each character in the hashmap
        # If at any point the count of a character becomes negative or if the strings have different lengths, they cannot be anagrams
        # after iterating through the second string check if all the counts in the hashmap are zero
        # If they are then the strings are anagrams
        # If the lengths of the strings are different at the start return false early

        return sorted(s) == sorted(t)



        