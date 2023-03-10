class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    # naive solution (slow) O(n^3)
    result = set()
    from itertools import combinations
    for i, j, k in combinations(nums, 3):
      total = i + j + k
      if not (total == 0): continue
      result.add(tuple(sorted([i, j, k])))
    return [list(tup) for tup in result]

  
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    # all exceptions and possibilities filtered method O(n^2)
    # https://leetcode.com/problems/3sum/solutions/725950/python-5-easy-steps-beats-97-4-annotated/
    result = set()

    positives = []
    negatives = []
    zeros = []

    for number in nums:
      if number > 0:
        positives.append(number)
      elif number < 0:
        negatives.append(number)
      else:
        zeros.append(number)
      
    positive_set = set(positives)
    negative_set = set(negatives)

    if zeros:
      for positive in positive_set:
        if - positive in negative_set:
          result.add((- positive, 0, positive))

      if len(zeros) >= 3:
        result.add((0, 0, 0))
    
    from itertools import combinations

    for i, j in combinations(positives, 2):
      if - (i + j) in negative_set:
        result.add(tuple(sorted([- (i + j), i, j])))

    for i, j in combinations(negatives, 2):
      if - (i + j) in positive_set:
        result.add(tuple(sorted([- (i + j), i, j])))
    
    return [list(tup) for tup in result]


  def threeSum(self, nums: list[int]) -> list[list[int]]:
    # two pointer binary search method O(n^2)
    # https://leetcode.com/problems/3sum/solutions/3109452/c-easiest-beginner-friendly-sol-set-two-pointer-approach-o-n-2-time-and-o-n-space/
    nums.sort()
    result = set()
    for i in range(len(nums)):
      j = i + 1
      k = len(nums) - 1
      while j < k:
        total = nums[i] + nums[j] + nums[k]
        if total > 0:
          k -= 1
        elif total < 0:
          j += 1
        else:
          result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
          j += 1
    return [list(tup) for tup in result]


# print(Solution().threeSum([-1,0,1,2,-1,-4]))
inputt = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
print("inp:", inputt)
result = Solution().threeSum(inputt)
print("res:", result)
expected_result = [[-4, 1, 3], [-4, 4, 0], [-2, 1, 1], [-2, 4, -2], [1, -5, 4], [0, 0, 0]]
print("exp:", expected_result)
print("correct:", expected_result == result)