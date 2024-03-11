class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = [asteroids[0]]
        
        for asteroid in asteroids[1:]:
            is_empty = len(res) == 0
            is_ast_left = asteroid < 0
            is_last_left = is_empty or res[-1] < 0
            is_ast_right = asteroid > 0
            
            if (is_ast_right) or (is_ast_left and is_last_left):
                res.append(asteroid)
                continue
            
            while is_ast_left and not is_last_left:
                last = res.pop()
                absolute = abs(asteroid)
                
                if absolute == last:
                    break
                elif absolute < last:
                    res.append(last)
                    break
                else:
                    is_empty = len(res) == 0
                    is_last_left = is_empty or res[-1] < 0
                    if is_last_left:
                        res.append(asteroid)
                        break
            
        return res