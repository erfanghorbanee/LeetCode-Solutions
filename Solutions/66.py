
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        result = int("".join(map(str, digits))) + 1
        return [int(i) for i in str(result)]