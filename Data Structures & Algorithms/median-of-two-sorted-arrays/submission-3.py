class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            a, b = nums2, nums1
        else:
            a, b = nums1, nums2
        total_size = len(a) + len(b)
        half = total_size//2
        l, r = 0, len(a)-1
        while True:
            i = (l+r)//2
            j = half-i-2
            Aleft = a[i] if i >= 0 else float("-infinity")
            Aright = a[i+1] if (i+1) < len(a) else float("infinity")
            Bleft = b[j] if j >= 0 else float("-infinity")
            Bright = b[j+1] if j+1<len(b) else float("infinity")
            if Aleft <= Bright and Bleft <= Aright:
                if total_size %2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1