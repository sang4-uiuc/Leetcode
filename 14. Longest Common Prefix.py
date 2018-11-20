def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    
                    return shortest[:i]
        return shortest 

print(longestCommonPrefix(["hello", "hemoglobe", "heinous"]))