class Solution:
    """
    Using Binary Search
    Time Complexity: O(Log(X))
    """

    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        result = 0

        while l <= r:
            m = l + ((r - l) // 2)

            if m**2 > x:
                r = m - 1
            elif m**2 < x:
                l = m + 1
                result = m
            else:
                return m

        return result
