# Uses python3
import sys

#def optimal_sequence(n):
#    sequence = []
#    while n >= 1:
#        sequence.append(n)
#        if n % 3 == 0:
#            n = n // 3
#        elif n % 2 == 0:
#            n = n // 2
#        else:
#            n = n - 1
#    return reversed(sequence)

def optimal_sequence(n):
    rec = {k:v for (k,v) in enumerate(fewest_operations(n))}
    sequence = []
    while n >= 1:
        sequence.append(n)
        if (n % 3 == 0 and n % 2 == 0):
            if rec[n//3] == rec[n]-1:
                n = n//3
                continue
            if rec[n//2] == rec[n]-1:
                n = n//2
                continue
            if rec[n-1] == rec[n]-1:
                n = n-1
        elif (n % 3 == 0):
            if rec[n//3] == rec[n]-1:
                n = n//3
                continue
            if rec[n-1] == rec[n]-1:
                n = n-1        
        elif (n % 2 == 0):
            if rec[n//2] == rec[n]-1:
                n = n//2
                continue
            if rec[n-1] == rec[n]-1:
                n = n-1
        else:
            n = n-1
    return reversed(sequence)
        
def fewest_operations(n):
    table = [None]*(n+1)
    table[0], table[1] = 0,0
    # table[0] corresponds to number 0
    # recurrence fewest_operations(n) = min(fewest_operations(n//3),
    # fewest_operations(n//2), fewest_operations(n-1)) + 1
    for i in range(2,n+1):
        if (i % 3 == 0 or i % 2 == 0):
            if i%3 != 0:
                table[i] = 1+min(table[i-1],table[i//2])
            elif i%2 != 0:
                table[i] = 1+min(table[i-1],table[i//3])
            else:
                table[i] = 1+min(table[i-1],table[i//2],table[i//3])
        else:
            table[i] = 1+table[i-1]
    return table

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
