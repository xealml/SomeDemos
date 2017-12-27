class Solution:
    def optimalDivision(self,nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0]/nums[1]
        tmp = 0
        for _ in nums[2:]:
            tmp += _
        return nums[0]/nums[1] * tmp
    def optimalDivision2(self,nums):
        result = ''

        if len(nums) == 1:
            result = str(nums[0])
        elif len(nums) == 2:
            result = str(nums[0]) + '/' + str(nums[1])
        else:
            result += str(nums[0]) + '/('
            for _ in nums[1:-1]:
                result += str(_) + '/'
            result += str(nums[-1]) + ')'
        return result

s = Solution()
print(s.optimalDivision2([1,2,3]))

