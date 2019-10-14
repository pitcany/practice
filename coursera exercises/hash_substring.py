# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences_old(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def get_occurrences(pattern, text):
    result = []
    len_pattern = len(pattern)
    len_text = len(text)
    hash_text, hash_pattern = generate_hash(pattern, text)
    if text[:len_pattern] == pattern:
        result.append(0)
    for i in range(1,len_text-len_pattern+1):
        if hash_text[i] == hash_pattern:
            if text[i:i+len_pattern] == pattern:
                result.append(i)
    return result

def generate_hash(pattern, text):
    ord_text = [ord(i) for i in text] # unicode values of characters in text
    ord_pattern = [ord(j) for j in pattern] # likewise for pattern
    len_text, len_pattern = len(text), len(pattern)
    hash_pattern = sum(ord_pattern)
    len_hash_array = len_text - len_pattern + 1
    # length of new array with hash values of text
    hash_text = [0]*len_hash_array
    for i in range(len_hash_array):
        if i == 0:
            hash_text[i] = sum(ord_text[:len_pattern])
            # initial value of hash function
        else:
            hash_text[i] =((hash_text[i-1]-ord_text[i-1]) + 
                     ord_text[i+len_pattern-1])
            # calculate next hash value
    
    return [hash_text, hash_pattern] # return hash values

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

