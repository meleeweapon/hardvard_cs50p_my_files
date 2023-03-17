def main() -> None:
  # Solution().lengthOfLongestSubstring("abcabcbb")
  # Solution().lengthOfLongestSubstring(" ")
  print(Solution().lengthOfLongestSubstring("abcabc"))
  print(Solution().lengthOfLongestSubstring("bbbbb"))
  ...

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


  def lengthOfLongestSubstring(self, s: str) -> int:
    head_poiner = 0
    tail_pointer = 0
    print("fjdskl")

    for _ in range(len(s)):
      tail_pointer += 1
      temp = s[head_poiner:tail_pointer]
      if self.has_repeating_characters(temp):
        head_poiner += 1
    
    return tail_pointer - head_poiner
  
  def has_repeating_characters(self, s: str) -> bool:
    return len(set(s)) != len(s)


  def lengthOfLongestSubstring(self, s: str) -> int:
    sliding_window = set()
    max_len, head_pointer = 0, 0
    for tail_pointer in range(len(s)):
      while s[tail_pointer] in sliding_window:
        sliding_window.remove(s[head_pointer])
        head_pointer += 1
      sliding_window.add(s[tail_pointer])
      max_len = max(max_len, tail_pointer - head_pointer + 1)
    return max_len


if __name__ == '__main__':
  main()