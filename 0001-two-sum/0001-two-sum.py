class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs = []

        # for num in nums:
        #     pair_num = target - num  # target num을 만들 수 있는 원소

        #     if pair_num in nums and num == pair_num:
        #         indexs = [i for i, value in enumerate(nums) if value == num]
        #         if len(indexs) > 1 and indexs[0] != indexs[1]:
        #             return indexs
        #     elif pair_num in nums:
        #                 return [nums.index(num), nums.index(pair_num)]

        # hash table 사용
        vals = {}
        for i in range(len(nums)):
            if nums[i] in vals:
                return [vals[nums[i]], i]
            vals[target - nums[i]] = i
