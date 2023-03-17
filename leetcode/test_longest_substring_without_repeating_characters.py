import longest_substring_without_repeating_characters as s

def test_lengthOfLongestSubstring():
  len_of = s.Solution().lengthOfLongestSubstring
  assert len_of("abcabcbb") == 3
  assert len_of("bbbbb") == 1
  assert len_of("pwwkew") == 3
  assert len_of("") == 0
  assert len_of(" ") == 1

test_lengthOfLongestSubstring()