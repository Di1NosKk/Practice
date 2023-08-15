#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        if digits == "":
            return []
        
        def dfs(combination, nextdigit):
            if nextdigit == "":
                res.append(combination)
            else: 
                for i in dic[nextdigit[0]]:
                    dfs(combination + i, nextdigit[1:])
        res = []
        dfs("", digits)
        return res
# @lc code=end

