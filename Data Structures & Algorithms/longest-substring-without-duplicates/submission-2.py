class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        char_freq = set()
        left = 0
        for right in range(len(s)):
            while s[right] in char_freq:
                char_freq.remove(s[left])
                left+=1
            char_freq.add(s[right])
            length = max(length, right-left +1)
        return length