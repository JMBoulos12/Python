



"""
  Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
  
  Example 1:
  Input: n = 3
  Output: ["((()))","(()())","(())()","()(())","()()()"]
  
  Example 2:
  Input: n = 1
  Output: ["()"]
  
  Constraints:
  1 <= n <= 8 
  07-February-2023
"""

class Solution:
  def generateParenthesis(self, n):
    ans = []

    def dfs(l: int, r: int, s: str) -> None:
      if l == 0 and r == 0:
        ans.append(s)
      if l > 0:
        dfs(l - 1, r, s + '(')
      if l < r:
        dfs(l, r - 1, s + ')')

    dfs(n, n, '')
    return ans

  
  
  
  
  
