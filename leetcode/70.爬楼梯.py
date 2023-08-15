#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [1, 2]
        for i in range(2, n+1):
            ans.append(ans[i-1]+ans[i-2])
        return ans[n-1]
# @lc code=end

