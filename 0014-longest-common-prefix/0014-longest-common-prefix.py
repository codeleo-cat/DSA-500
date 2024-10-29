class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        minStr = min(strs, key=len)

        for i, el in enumerate(minStr):
            for other in strs:  # 특정 원소
                if other[i] != el:
                    return minStr[:i]
        return minStr