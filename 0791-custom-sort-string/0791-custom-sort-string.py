class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {}
        
        for i, char in enumerate(order):
            order_dict[char] = i
        
        sorted_s = sorted(list(s), key = lambda x: order_dict.get(x, -1))
        return "".join(sorted_s)