
class Solution:
    #시간복잡도 O(n)
    def maxProfit(self, prices: List[int]) -> int:
        #이 문제에서는 0으로 처리해도 문제없었지만 sys.maxsize로 처리하는 것이 더 정확
        buy = 0
        sell = 0
        
        outputs = []
        buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy:
                outputs.append(sell-buy)
                buy = prices[i]
                sell = 0
            elif prices[i] > sell and prices[i] - buy > 0:
                sell = prices[i]

        #output 배열을 만들어 마지막에 max를 처리하는 게 아니라 계속해서 max로 갱신해나가면 공간복잡도를 줄일 수 있음
        #(최소 가격과 이익을 계속 갱신해나가는 방식)
        outputs.append(sell-buy)
        max_money = max(outputs)
        if max_money <= 0:
            return 0
        else:
            return max_money
        