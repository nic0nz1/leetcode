class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        res = []
        for i in range(len(nums)):
            if i %2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort(reverse=True)
        odd.sort()
        while even and odd:
            res.append(even.pop())
            res.append(odd.pop())
        if odd:
            res.append(odd.pop())
        if even:
            res.append(even.pop())
        return res
