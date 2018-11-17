class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        
        for index in range(len(haystack)):
            if haystack[index] == needle[0]:
                if haystack[index:index + len(needle)] == needle:
                    return index
        return -1