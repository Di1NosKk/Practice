#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution: 
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = 0
        ## 12 * 4     12 * 10  2*3
        for i in range(len(num1)):
            tmp = 0
            for j in range(len(num2)):
                tmp += int(num1[i]) * (10 ** i) * int(num2[j]) * (10 ** j)
            ans += tmp
        return str(ans)
# @lc code=end

