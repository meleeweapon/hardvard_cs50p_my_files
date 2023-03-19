class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      hits = 0
      t_ind = 0
      for s_char in s:
        while True:
          if t_ind >= len(t):
            break
          if s_char == t[t_ind]:
            t_ind += 1
            hits += 1
            break
          t_ind += 1
      return hits == len(s)



# print(Solution().isSubsequence("abc", "ahbgdc"))
# print(Solution().isSubsequence("axc", "ahbgdc"))
print(Solution().isSubsequence("aaaaaa", "bbaaaa"))