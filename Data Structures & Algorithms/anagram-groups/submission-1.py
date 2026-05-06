class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {} 

        for str in strs:
            key = ''.join(sorted(str))
            if not key in h:
                h[key] = [str]
            else:
                h[key].append(str)
        return (list(h.values()))