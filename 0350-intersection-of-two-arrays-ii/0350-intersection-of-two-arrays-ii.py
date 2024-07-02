class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        m = len(nums1)
        n = len(nums2)

        ptr1 = 0
        ptr2 = 0

        ans = []

        while ptr1 < m and ptr2 < n:
            if nums1[ptr1] == nums2[ptr2]:
                ans.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1

        return ans