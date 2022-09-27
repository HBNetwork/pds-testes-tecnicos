"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in
the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


def has_duplicate(nums):
    existing_nums = set()
    for num in nums:
        if num in existing_nums:
            return True
        existing_nums.add(num)
    return False


def has_duplicate(nums):
    return len(nums) != len(set(nums))


def has_duplicate(nums):
    nums.sort() #O(nlogn)

    return any(current == next_ for current, next_ in zip(nums[:-1], nums[1:]))


def has_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


# def has_duplicate(nums):
#     seen = set()
#     for n in nums:
#         if n not in seen:
#             seen.add(n)
#             continue
#         return True
#     return False



if __name__ == "__main__":
    assert has_duplicate([1, 2, 3, 1]) == True
    assert has_duplicate([1, 2, 3, 4]) == False
    assert has_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert has_duplicate([1]) == False
    assert has_duplicate([1] * 10**5) == True
    assert has_duplicate(list(range((10 ** 5) + 1))) == False
    #assert has_duplicate(list(range(-10**9, 10**9))) == False


    """
    Explicação do hashtable tosqueira.
    
    hashtable = [None] * 26

    def hashfunc(string):
        letra = string[0]
        return ord(letra) - 97

    def store(string):
        idx = hashfunc(string)
        hashtable[idx] = string

    store("andre")
    store("henrique")
    print(hashtable)
    """
