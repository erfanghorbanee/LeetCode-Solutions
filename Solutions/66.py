
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        result = int("".join(map(str, digits))) + 1
        return [int(i) for i in str(result)]


# Optimized version modifying digits in place
# first solution works perfectly but converts back and forth between data types,
# which can be costly in time and space for large inputs. This version operates
# directly on the input list without extra conversions.
class SolutionOptimized:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If loop completes, all digits were 9, so prepend 1
        return [1] + digits