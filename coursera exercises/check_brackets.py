# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    indices_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            indices_stack.append(i)
            opening_brackets_stack.append(next)
        elif next in ")]}":
            if not opening_brackets_stack:
                return i+1
            top = opening_brackets_stack.pop()
            indices_stack.pop()
            if not are_matching(top,next):
                return i+1
    return min(indices_stack)+1 if indices_stack else 'Success'

find_mismatch('[][')

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
