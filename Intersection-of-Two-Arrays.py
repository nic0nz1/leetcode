class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = set()
        nums1pointer = 0
        nums2pointer = 0
        while nums1pointer < len(nums1) and nums2pointer < len(nums2):
            if nums1[nums1pointer] == nums2[nums2pointer]:
                res.add(nums1[nums1pointer])
                nums1pointer += 1
                nums2pointer += 1
            elif nums1[nums1pointer] < nums2[nums2pointer]:
                nums1pointer += 1
            else:
                nums2pointer += 1
        return list(res)


