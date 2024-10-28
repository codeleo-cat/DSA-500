class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        cnt = 0
        major = None
        for n in nums:
            if cnt == 0:
                major = n
            if n == major:
                cnt +=1
            else:
                cnt -=1
        return major