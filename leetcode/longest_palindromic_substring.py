# TODO: time limit exceeded error, optimize

class Solution:
  def longestPalindrome(self, s: str) -> str:
    if len(s) < 2:
      return s

    temp = s[0]
    for sub_len in range(2, len(s) + 1):
      for i in range(len(s) - sub_len + 1):
        sub_str = s[i:i + sub_len]
        if self.is_palindromic(sub_str):
          temp = sub_str
    return temp


  def is_palindromic(self, s: str) -> bool:
    s_len = len(s)
    for i in range(s_len//2):
      if s[i] != s[s_len - 1 - i]:
        return False
    return True
