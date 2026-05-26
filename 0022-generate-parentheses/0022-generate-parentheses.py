class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def is_valid(string):
            count = 0
            for char in string:
                if char == "(":
                    count += 1
                else:
                    count -= 1
                
                # More closing brackets than opening ones at any point
                if count < 0:
                    return False

            # Must have exactly equal opening and closing brackets
            return count == 0

        def solve(string):
            # Base Case: Sequence length is 2*n
            if len(string) == 2 * n:
                if is_valid(string):
                    result.append("".join(string))
                return

            # Choice 1: Add an opening bracket
            string.append("(")
            solve(string)
            string.pop() # Backtrack

            # Choice 2: Add a closing bracket
            string.append(")")
            solve(string)
            string.pop() # Backtrack

        # Start recursion with an empty list
        solve([])

        return result
        