class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        for i in range(1, n + 1):
            expr1 = i % 3
            expr2 = i % 5

            if not expr1 and not expr2:
                result.append("FizzBuzz")

            elif not expr1:
                result.append("Fizz")

            elif not expr2:
                result.append("Buzz")

            else:
                result.append(str(i))

        return result
