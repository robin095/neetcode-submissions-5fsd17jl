class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in range (len(operations)):
            if operations[i]!= "+" and operations[i]!="D" and operations[i]!="C":
                score.append(int(operations[i]))
            elif operations[i] == "+":
                score.append(score[-2] + score[-1])
            elif operations[i] == "D":
                score.append(2*score[-1])
            elif operations[i] == "C":
                score.pop()
        return sum(score)    