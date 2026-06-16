class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        main_freq = Counter(s1)
        sec_freq = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            sec_freq[s2[right]] += 1
            if right - left + 1 > len(s1):
                sec_freq[s2[left]] -= 1
                if sec_freq[s2[left]] == 0:
                    del sec_freq[s2[left]]
                left += 1
            if right - left + 1 == len(s1):
                if sec_freq == main_freq:
                    return True
        return False