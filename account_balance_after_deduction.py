class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        fpn = float(purchaseAmount) / 10
        intmul0 = round(fpn)
        return (int(100 - (intmul0 * 10)))        