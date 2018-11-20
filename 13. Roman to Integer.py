class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ref = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
        }
        total = 0
        for i in range(len(s) - 1):
            if ref[s[i]] >= ref[s[i + 1]]:
                total += ref[s[i]]
            else:
                total -= ref[s[i]]
        
        return total + ref[s[-1]]