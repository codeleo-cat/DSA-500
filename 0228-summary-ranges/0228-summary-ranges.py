class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        output = []
        start = nums[0]  # 구간의 시작 값 초기화

        for i in range(1, len(nums) + 1):
            # 끝에 도달했거나 연속 구간이 끊어질 때
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                # 시작 값과 끝 값이 같으면 단일 값으로 추가
                if start == nums[i - 1]:
                    output.append(str(start))
                else:
                    output.append(f"{start}->{nums[i - 1]}")
                # 새로운 구간의 시작 값을 설정
                if i < len(nums):
                    start = nums[i]
        return output