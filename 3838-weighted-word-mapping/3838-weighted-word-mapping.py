class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        for word in words:
            res += self.mapWord(word, weights)
        return res
    def mapWord(self, word, weights):
        n = len(word)
        sum = 0
        for i in range(n):
            sum += weights[ord(word[i]) - 97]  
        return chr(122 - (sum % 26))
