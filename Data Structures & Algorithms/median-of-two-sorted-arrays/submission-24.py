class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a
        total_len = len(a) + len(b)
        half = total_len//2
        l = 0
        r = len(a)-1
        while True:
            midA = (l+r)//2
            midB = half-midA-2
            Aleft = a[midA] if midA >= 0 else float("-inf")
            Aright = a[midA+1] if midA+1 < len(a) else float("inf")
            Bleft = b[midB] if midB >= 0 else float("-inf")
            Bright = b[midB+1] if midB+1 < len(b) else float("inf")
            if Aleft <= Bright and Bleft <= Aright:
                if total_len%2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = midA - 1
            else:
                l = midA + 1
        return