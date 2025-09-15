class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        n_choose = nums[0]
        distance_min = abs(0 - n_choose)
        for n in nums[1:]:
            if abs(0 - n) < distance_min:
                distance_min = abs(0 - n)
                n_choose = n
            elif abs(0 - n) == distance_min:
                if n > n_choose:
                    distance_min = abs(0 - n)
                    n_choose = n

        return n_choose