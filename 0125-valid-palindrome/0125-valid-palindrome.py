class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        matched_s = [el for el in s if el.isalnum()]
        return matched_s[:] == matched_s[::-1]