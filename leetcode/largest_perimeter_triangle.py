from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
      from itertools import combinations
      for x, y, z in combinations(nums, 3):
         print(x, y, z)
         print(not (x >= y + z))
         print(not (y >= x + z))
         print(not (z >= y + x))
      perimeters = [
        x + y + z 
        for x, y, z in combinations(nums, 3)
        if not (x >= y + z) and not (y >= x + z) and not (z >= x + y)
      ]
      print(perimeters)
      return max(perimeters, default=0)
Solution().largestPerimeter([1,2,1,10])