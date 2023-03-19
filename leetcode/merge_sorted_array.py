from typing import List
class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if m < 1:
        for i, x in enumerate(nums2):
          nums1[i] = x
        return

    nums1_ind, nums2_ind = 0, 0
    while nums1_ind < m and nums2_ind < n:
      if nums2[nums2_ind] < nums1[nums1_ind]:
        self.insert(nums1, nums1_ind, nums2[nums2_ind])
        nums1_ind += 1
        nums2_ind += 1
      else:
        nums1_ind += 1
    
    # nums1_ind = m + nums2_ind
    # for i in range(m - n):
    while nums2_ind < n:

      # m + n - nums2_ind
      if nums1[nums1_ind] > nums2[nums2_ind]:
        self.insert(nums1, nums1_ind, nums2[nums2_ind])
        nums1_ind += 1
        nums2_ind += 1
      else:
        if nums1_ind != len(nums1) - 1:
          nums1_ind += 1
        nums1[nums1_ind] = nums2[nums2_ind]
        nums2_ind += 1

  def insert(self, array, index, value):
    i = index
    temp = 0
    temp_2 = value
    while i < len(array):
      temp = array[i]
      array[i] = temp_2
      temp_2 = temp
      i += 1

a1 = [1,2,3,0,0,0]
a2 = [2,5,6]
Solution().merge(a1, 3, a2, 3)
print(a1)

a1 = [4,0,0,0,0,0]
a2 = [1,2,3,5,6]
Solution().merge(a1, 1, a2, 5)
print(a1)

a1 = [1,0]
a2 = [2]
Solution().merge(a1, 1, a2, 1)
print(a1)

a1 = [0,0,0,0,0]
a2 = [1,2,3,4,5]
Solution().merge(a1, 0, a2, 5)
print(a1)


# mfdsa = [1,2,3,0]
# Solution().insert(mfdsa, 1, 5)
# print(mfdsa)