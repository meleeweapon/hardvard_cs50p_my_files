class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False

      char_map = {}
      for s_char, t_char in zip(s, t):
        if s_char in char_map:
           if t_char != char_map[s_char]:
            return False
        else:
          char_map[s_char] = t_char
      
      return (
        self.all_unique(char_map.keys()) and 
        self.all_unique(char_map.values())
      )
      
      # char_map = {s_char: t_char for s_char, t_char in zip(s, t)}
      # print(char_map)
      # return (
      #    (self.all_unique(char_map.keys()) and self.all_unique(char_map.values())) and
      #    (len(char_map.keys()) == len(char_map.values()))

      # )

      # for s_char, t_char in zip(s, t):
      #   if s_char in char_map:
      #      if t_char != char_map[s_char]:
      #       return False
      #   else:
      #     if t_char in char_map.values():
      #       return False
      #     char_map[s_char] = t_char
      
      # if (
      #   len(set(char_map.keys())) == len(char_map.keys()) and 
      #   len(set(char_map.values())) == len(char_map.values())
      # ):
      #   return True
      # return False

    def all_unique(self, obj):
      temp = {}
      for item in obj:
        if item in temp:
          return False
        temp[item] = 1
      return True
        


f = Solution().isIsomorphic
print(f("add", "egg"))
print(f("foo", "bar"))
print(f("badc", "baba"))