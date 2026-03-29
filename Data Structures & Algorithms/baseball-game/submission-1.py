class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i].isnumeric():
                record.append(int(operations[i]))
            elif operations[i][0] == '-':
                record.append(-1*int(operations[i][1:]))
            elif operations[i] == '+':
                record.append(record[-2] + record[-1])
            elif operations[i] == 'C':
                record.pop()
            elif operations[i] == 'D':
                record.append(record[-1]*2)

        print(record)
        return sum(record)