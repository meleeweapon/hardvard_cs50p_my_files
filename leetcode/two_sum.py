def main() -> None:
  ...

class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    needed_number = {target - number: index for index, number in enumerate(nums)}
    for index, number in enumerate(nums):
      if number in needed_number:
        if needed_number[number] != index:
          return [needed_number[number], index]


if __name__ == '__main__':
  main()