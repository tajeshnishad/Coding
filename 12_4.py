# using continue in a loop
current_count = 0
while current_count < 10:
    current_count += 1
    if current_count % 2 == 0:
        continue
    print(current_count)

print("\n")

# Avoiding Infinite Loop 
x = 1
while x <= 5:
    print(x)
    x += 1