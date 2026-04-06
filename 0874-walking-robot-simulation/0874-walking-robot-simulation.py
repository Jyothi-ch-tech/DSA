class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int: 
        x = 0
        y = 0
        i = 0
        d = 0 
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        obstacles = set(map(tuple, obstacles))
        ans = 0
        while i < len(commands):
            if commands[i] == -1:
                d = (d + 1) % 4
            elif commands[i] == -2:
                d = (d - 1) % 4
            else:
                dx, dy = dirs[d]
                step = 0
                while step < commands[i]:
                    if (x + dx, y + dy) in obstacles:
                        break
                    x += dx
                    y += dy
                    ans = max(ans, x*x + y*y)
                    step += 1
            i += 1
        return ans