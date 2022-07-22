class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max = 0
        for account in accounts:
            sum_account = sum(account)

            if sum_account > max:
                max = sum_account

        return max
