#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # return [int(item) for item in str(int("".join([str(item) for item in digits])) + 1)]
        number = int("".join([str(item) for item in digits]))
        res = str(number + 1)
        ans = []
        for i in res:
            ans.append(int(i))

        return ans
# @lc code=end

