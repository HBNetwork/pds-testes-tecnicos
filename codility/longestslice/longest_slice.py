"""
We call an array switching if all numbers in even positions are equal and all numbers in odd positions are equal.

For example: [3,-7,3,-7,3] and [4,4,4] are switching, but [5,5,4,5,4] and [-3,2,3] are not switching

What is the length of the longest switching slice (continuous fragment) in a given array A?

Write a function:

  class Soluction { public int solution(int[] A); }

that, given an array A consisting of N integers, returns the length of the longest switching slice in A.

Examples:

1. Given A = [3,2,3,2,3] the function should return 5, because the whole array is switching.

2. Given A = [7,4,-2,4,-2,-9], the function should return 4. The longest switching slice is [4,-2,4,-2].

3. Given A = [7, -5, -5, -5, 7, -1, 7], then function should return 3. There are two switching slices of equal length: [-5,-5,-5] and [7,-1,7]

4. Given A = [4], the function should return 1. A single-element slice is also a switching slice.

Write an eficient algorithm for the following assumptions:

  . N is an integer within the range[1..100,000];
  . each element of array is an integer within the range[-1,000,000,000..1,000,000,000]
"""
from array import array


def longest_slice(nums: array) -> int:
  if len(nums) <= 2:
    return len(nums)

  even = nums[0]
  odd = nums[1]

  size = 2
  longest = 2

  for i in range(2, len(nums), 2):
    n = nums[i]
    if n == even:
      size += 1
      if (size > longest):
        longest = size
    else:
      even = n
      max = 2
    
    if i + 1 < len(nums):
      if nums[i + 1] == odd:
        size += 1
        if (size > longest):
          longest = size
      else:
        odd = nums[i + 1]
        size = 2
    

  return longest

def main():
  assert longest_slice([4]) == 1
  assert longest_slice([4, 4]) == 2
  assert longest_slice([4, 4, 4]) == 3
  assert longest_slice([3, 2, 3, 2, 3]) == 5
  assert longest_slice([7, 4, -2, 4, -2, -9]) == 4
  assert longest_slice([7, -5, -5, -5, 7, -1, 7]) == 3
  assert longest_slice([4]) == 1

if __name__ == "__main__":
  main()
  print("Success!")
