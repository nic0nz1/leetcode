1class Solution:
2    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
3        #flatten matrix
4        all_nums = [item for sublist in matrix for item in sublist]
5        negatives = 0
6        #count negatives
7        for num in all_nums:
8            if num < 0:
9                negatives += 1
10        #create abs array
11        positive_all_nums = [abs(num) for num in all_nums]
12        #sort abs array
13        positive_all_nums.sort()
14        #get sum
15        result = sum(positive_all_nums)
16        #return da answer
17        return result if negatives % 2 == 0 else result - positive_all_nums[0] * 2