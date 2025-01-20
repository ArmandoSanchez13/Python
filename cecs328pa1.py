import sys

def sumdigits(num):
    return sum(int(digit) for digit in str(num)) 

def longest(n):
    maxlength = 0
    temp = {}
    i = 0
    for j in range(len(n)):
        current = sumdigits(n[j])
        if current in temp:
            i = max(i, temp[current])
        maxlength = max(maxlength, j - i + 1)
        temp[current] = j + 1
    return maxlength

if __name__ == "__main__":
    input = sys.argv[1]
    try:
        with open(input, 'r') as file:
            n = [int(line.strip()) for line in file]
            print(longest(n))
    except FileNotFoundError:
        print(f"Error: File '{input}' not found.")
        sys.exit(1)

