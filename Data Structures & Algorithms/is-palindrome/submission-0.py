class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = "".join(char for char in s if char.isalnum())
        print(result)
        left = 0
        right = len(result)-1
        while left < right:
            if result[left] != result[right]:
                return False
            left+=1
            right-=1
        return True
        