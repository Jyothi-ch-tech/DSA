class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        box=boxGrid
        m, n = len(box), len(box[0])
        for row in box:
            empty_slot = n - 1 
            for col in range(n - 1, -1, -1):
                if row[col] == '#': 
                    row[col], row[empty_slot] = row[empty_slot], row[col]
                    empty_slot -= 1
                elif row[col] == '*': 
                    empty_slot = col - 1
        rotated_box = [[None] * m for _ in range(n)] 
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - 1 - i] = box[i][j]
        
        return rotated_box
        