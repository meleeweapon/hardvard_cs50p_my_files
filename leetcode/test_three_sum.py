from three_sum import *

def test_three_sum():
  three_sum = Solution().threeSum
  # assert three_sum([-1,0,1,2,-1,-4]) == set(set(-1,-1,2),set(-1,0,1))
  # test_1 = three_sum([-1,0,1,2,-1,-4])
  # assert [-1, -1, 2] in test_1 and [-1, 0, 1] in test_1
  assert three_sum([0,1,1]) == []
  assert three_sum([0,0,0]) == [[0,0,0]]