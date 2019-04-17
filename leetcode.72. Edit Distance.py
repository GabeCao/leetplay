class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1 = list(word1)
        word2 = list(word2)

        dp = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        for i in range(len(word2)+1):
            dp[i][0] = i
        for j in range(len(word1)+1):
            dp[0][j] = j

        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(min(dp[i-1][j-1]+1, dp[i-1][j]+1), dp[i][j-1]+1)
        return dp[len(word2)][len(word1)]

if __name__ == '__main__':
    sl = Solution()
    word1 = 'intention'
    word2 = 'execution'
    print(sl.minDistance(word1, word2))