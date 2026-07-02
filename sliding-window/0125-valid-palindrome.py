"""
LeetCode 125 - Valid Palindrome

Difficulty: Easy
Pattern: Two Pointers

Brute Force:
Time Complexity: O(n)
Space Complexity: O(n)

Optimal:
Time Complexity: O(n)
Space Complexity: O(1)

Key Idea:
Use two pointers starting from both ends of the string. Skip any non-alphanumeric
characters and compare the remaining characters case-insensitively. If a mismatch
is found, the string is not a palindrome. Otherwise, continue moving the pointers
toward the center until they meet or cross.

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left<right:
            while left<right and not self.isAlphanumeric(s[left]):
                left +=1
            while left<right and not self.isAlphanumeric(s[right]):
                right-=1
        
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True 
       
    
    def isAlphanumeric(self, char):
        return (
            ord("A")<=ord(char)<=ord("Z") or
            ord("a")<=ord(char)<=ord("z") or
            ord("0")<=ord(char)<=ord("9")
        )
