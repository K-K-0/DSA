class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        len1 = len(nums1)
        len2 = len(nums2)

        i = 0
        j = 0


        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        arr.extend(nums1[i:])
        arr.extend(nums2[j:])
        
        n = len1 + len2
        if n % 2 == 1:
            return float(arr[n // 2])
        
        median = (arr[n // 2] + arr[(n // 2) - 1]) / 2.0
        return median