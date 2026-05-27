class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master_hash = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            master_hash[sorted_str].append(str)
        return list(master_hash.values())