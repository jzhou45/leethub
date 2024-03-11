class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flipped = []
        curr_count = max_count = 0
        more_than_k = k == 0
         
        for i, num in enumerate(nums):
            if not more_than_k:
                if num == 0:
                    flipped.append(i)
                    if len(flipped) >= k: more_than_k = True
                max_count += 1
                curr_count += 1
            else:
                if num == 0:
                    if k == 0:
                        max_count = max(max_count,curr_count)
                        curr_count = 0
                    else:
                        new_start = flipped[0]
                        temp_count = i - new_start
                        max_count = max(max_count, temp_count, curr_count)
                        curr_count = temp_count
                        flipped = flipped[1:]
                        flipped.append(i)
                else:
                    curr_count += 1
                    
        return max(curr_count, max_count)