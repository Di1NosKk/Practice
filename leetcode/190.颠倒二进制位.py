#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        n = '{:032b}'.format(n)
        n = n[::-1]
        return int(n,2)
# @lc code=end

