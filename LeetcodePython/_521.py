class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        lena = len(a)
        lenb = len(b)
        if lena != lenb:
            return len(a) if len(a) > len(b) else len(b)
        else:
            if a == b:
                return -1
            return len(a)
    def findLUSlength2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        lena = len(a)
        lenb = len(b)
        if len(a) != len(b):
            return len(a) if len(a) > len(b) else len(b)
        return -1 if a == b else len(a)
    def findLUSlength3(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        lena = len(a)
        lenb = len(b)
        if lena != lenb:
            return lena if lena > lenb else lenb
        return -1 if a == b else lena


s = Solution()
print(s.findLUSlength(a='hello',b='hexxxxxx'))