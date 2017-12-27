class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x=0
        y=0
        for _ in moves:
            if _=='U':
                y += 1
            elif _=='D':
                y -= 1
            elif _=='L':
                x -= 1
            else:
                x += 1
        return x == 0 and y == 0
s = Solution()
print(s.judgeCircle("UD"))

for _ in "What the fuck is the mother fuck of you":
    print(_)
import requests
url = 'http://www.baidu.com'
txt = requests.get(url)
txt.encoding = 'utf-8'
print(txt.text)