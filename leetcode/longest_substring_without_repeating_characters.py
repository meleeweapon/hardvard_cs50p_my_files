def main() -> None:
  # Solution().lengthOfLongestSubstring("abcabcbb")
  Solution().lengthOfLongestSubstring(" ")


class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    longest_length = 0
    for outer_index in range(len(s)):
      current_substring = ""
      for char in s[outer_index:]:
        if char in current_substring:
          break
        current_substring += char
      longest_length = max(len(current_substring), longest_length)
    return longest_length

# TODO: implement the sliding window solution and the sliding window with hashmap of char to ind or count
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    ...
  
  def has_repeating_characters(self, s: str) -> bool:
    ...

if __name__ == '__main__':
  main()