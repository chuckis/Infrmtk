# Towers of Hanoi recursive solution

def hanoi(num_circles, a, b, c):
    if num_circles == 1:
        print(f'{a} -> {b}')
        return
    hanoi(num_circles-1, a, c, b)
    print(f'{a} -> {b}')
    hanoi(num_circles-1, c, b, a)

hanoi(3, "A", "B", "C")

# Output 
# A -> B
# A -> C
# B -> C
# A -> B
# C -> A
# C -> B
# A -> B
