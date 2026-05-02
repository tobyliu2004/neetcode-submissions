class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a)>len(b):
            a, b = b, a
        total_len = len(a)+len(b)
        half = total_len//2
        l = 0
        r = len(a)-1

        while True:
            i = (l+r)//2
            j = half-i-2
            Aleft = a[i] if i >= 0 else float("-infinity")
            Bleft = b[j] if j >= 0 else float("-infinity")
            Aright = a[i+1] if i+1 < len(a) else float("infinity")
            Bright = b[j+1] if j+1 < len(b) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total_len % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            else:
                if Aleft > Bright:
                    r = i-1
                else:
                    l = i + 1