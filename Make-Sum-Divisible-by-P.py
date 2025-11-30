1class Solution:
2    def minSubarray(self, nums: List[int], p: int) -> int:
3        prefix_sum = [nums[0]]
4        for i in range(1,len(nums)):
5            prefix_sum.append(nums[i] + prefix_sum[i-1])
6        
7        nums_sum = prefix_sum[-1]
8        if nums_sum % p == 0:
9            return 0
10        target_remainder = nums_sum % p
11        
12        min_length = inf
13        hashmap = {0:-1}
14        for i, v in enumerate(prefix_sum):
15            current_remainder = v % p
16            if (current_remainder - target_remainder + p) % p in hashmap:
17                print("FOUND!")
18                min_length = min(min_length, i - hashmap[(current_remainder - target_remainder + p) % p])
19            hashmap[v % p] = i
20        if min_length == len(nums):
21            return -1
22        return min_length if min_length != inf else -1