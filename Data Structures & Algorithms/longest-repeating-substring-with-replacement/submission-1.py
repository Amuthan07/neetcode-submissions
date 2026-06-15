class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0,0
        freq = defaultdict(int)
        longest = 0
        max_freq = 0

        while right < len(s):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])
            if (right - left + 1) -  max_freq > k:
                freq[s[left]] -= 1
                left += 1
            longest = max(longest, right-left+1)
            right += 1
        return longest