class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastone = None
        for i in range(len(nums)):
            if nums[i] == 1:
                if lastone == None:
                    lastone = i
                    continue
                if (i - lastone) < (k + 1):
                    return False
                lastone = i
        return True