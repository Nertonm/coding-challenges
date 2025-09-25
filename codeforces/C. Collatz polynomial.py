degree = int(input())
bits = int(input().replace(" ", "").strip(), 2)
steps = 0
        
while bits != 1:
    if bits & 1:
        bits = bits ^ (bits << 1 ) ^ 1
    else: 
        bits >>= 1
    steps += 1

print(steps)
