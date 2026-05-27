class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master_hash = {}
        for str in strs:
            count = [0]*26
            for char in str:
                count[ord(char)-ord('a')] += 1
            count=tuple(count)
            if count not in master_hash:
                master_hash[count] = []
            master_hash[count].append(str)
        return list(master_hash.values())