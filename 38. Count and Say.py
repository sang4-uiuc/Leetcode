class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        curr = '1'
        for i in range(n - 1):
            next = ""
            j = 0
            while j < len(curr):
                cnt = 1
                while j + 1 < len(curr) and curr[j] == curr[j+1]:
                    j += 1
                    cnt += 1
                next += str(cnt)
                next += curr[j]
                j += 1
            curr = next
        return curr
            
            