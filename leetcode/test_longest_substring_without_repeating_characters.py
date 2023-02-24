from longest_substring_without_repeating_characters import Solution

def test_lengthOfLongestSubstring():
  sln = Solution
  assert sln.lengthOfLongestSubstring(sln, "abcabcbb") == 3
  assert sln.lengthOfLongestSubstring(sln, "bbbbb") == 1
  assert sln.lengthOfLongestSubstring(sln, "pwwkew") == 3
  assert sln.lengthOfLongestSubstring(sln, "") == 0
  assert sln.lengthOfLongestSubstring(sln, " ") == 1