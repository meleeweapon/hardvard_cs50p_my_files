import two_sum

def test_two_sum():
  twoSum = two_sum.Solution().twoSum
  assert twoSum([2,7,11,15], 9) == [0, 1] or [1, 0]
  assert twoSum([3,2,4], 6) == [1, 2] or [2, 1]
  assert twoSum([3, 3], 6) == [0, 1] or [1, 0]