class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_1 = {}
        freq_2 = {}
        for char in s:
            if char not in freq_1:
                freq_1[char] = 1
            freq_1[char] += 1
        for char in t:
            if char not in freq_2:
                freq_2[char] = 1
            freq_2[char] += 1
        # print(freq_1)
        # print(freq_2)
        if freq_1 == freq_2:
            return True
        else:
            return False
        