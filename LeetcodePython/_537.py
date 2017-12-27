class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n0=int(a.split('+')[0])
        n1=int(a.split('+')[1].split('i')[0])
        m0=int(b.split('+')[0])
        m1=int(b.split('+')[1].split('i')[0])
        return str(n0*m0+n1*m1)+str('+')+str(n0*m1+n1*m0)+str('i')