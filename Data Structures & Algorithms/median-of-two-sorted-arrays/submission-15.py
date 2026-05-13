class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a)>len(b):
            a, b = b, a
        
        total = len(a) + len(b)
        middle = total//2

        l = 0
        r = len(a)-1

        while True:
            midA = (l+r)//2
            midB = middle-midA-2
            Aleft = a[midA] if midA >= 0 else float("-infinity")
            Aright = a[midA+1] if midA+1<len(a) else float("infinity")
            Bleft = b[midB] if midB >= 0 else float("-infinity")
            Bright = b[midB+1] if midB+1<len(b) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total%2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = midA - 1
            else:
                l = midA + 1