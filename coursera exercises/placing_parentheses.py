# Uses python3
import math
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_max(M, m, i, j, operators):
    min_val = math.inf
    max_val = -math.inf
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], operators[k])
        b = evalt(M[i][k], m[k+1][j], operators[k])
        c = evalt(m[i][k], M[k+1][j], operators[k])
        d = evalt(m[i][k], m[k+1][j], operators[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val

def get_maximum_value(dataset):
    #write your code here
    operators, operands = parse(dataset)
    n = len(operands)
    m = [[None for _ in range(n)] for _ in range(n)]
    M = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = min_max(M, m, i, j, operators)

    return M[0][n-1]
    return 0

def parse(expr):
    operators, operands = [], []
    for i in expr:
        if i in ['+','-','*']:
            operators.append(i)
        else:
            operands.append(int(i))
    return operators, operands

if __name__ == "__main__":
    print(get_maximum_value(input()))
