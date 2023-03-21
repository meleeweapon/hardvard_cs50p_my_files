from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      if numRows < 2:
        return [[1]]
      rows = [[1], [1, 1]]
      for _ in range(numRows - 2):
        row = [1]
        for x, y in zip(rows[-1], rows[-1][1:]):
          row.append(x + y)
        row.append(1)
        rows.append(row)
      return rows