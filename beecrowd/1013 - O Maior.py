# input: Three integer values
a, b, c = map(int, input().split())

# Determine the largest value using conditional statements
if b > a:
    a = b
if c > a:
    a = c

# Output the largest value
print(f"{a} eh o maior")