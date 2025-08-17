class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        lsum = 0 
        rsum = 0
        ridx = len(cardPoints) - 1

        for i in range(k):
            lsum += cardPoints[i]
        
        maxsum = lsum

        for i in range(k - 1, -1, -1):
            lsum -= cardPoints[i]

            rsum += cardPoints[ridx]

            ridx -= 1

            maxsum = max(maxsum, lsum + rsum)

        return maxsum


