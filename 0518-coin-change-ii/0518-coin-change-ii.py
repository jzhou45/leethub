class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        arr = [0] * (amount + 1) #[1,1,2,2,0,0]
        arr[0] = 1
        
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i: 
                    arr[i] = arr[i - coin] + arr[i] #arr[3] = arr[] + arr[3]
        
        return arr[-1]