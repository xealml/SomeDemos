class Solution:
    def detectCapitalUse(self,word):
        return word.islower() or word.istitle() or word.isupper()
S = Solution()
print(S.detectCapitalUse(word='hello'))
print(S.detectCapitalUse(word='HELLO'))
