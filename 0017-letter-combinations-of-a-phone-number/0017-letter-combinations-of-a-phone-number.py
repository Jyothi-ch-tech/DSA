class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            "9":"wxyz"
        }
        res=['']
        for i in range(len(digits)):
            current=d[digits[i]]
            new_res=[]
            for combo in res:
                for letter in current:
                    new_res.append(combo+letter)
            res=new_res
        return res

        