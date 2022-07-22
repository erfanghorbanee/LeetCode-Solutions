class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """

        n = num
        step = 0
        while True:
            if n == 0:
                return step

            if (n % 2) == 0:
                n = n / 2
            else:
                n -= 1

            step += 1
