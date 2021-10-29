from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_set = {}
        for i in range(len(nums)):
            num = nums[i]
            try:
                return [result_set[target - num], i]
            except KeyError:
                result_set[num] = i


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))
