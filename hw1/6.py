# Calculate A
A = sum(1/i**2 for i in range(1, 10001))

# Calculate B
B = sum(1/i**2 for i in range(10000, 0, -1))

print("Value of A:", A)
print("Value of B:", B)

#Compare
if A > B:
    print("A is greater than B")
elif A < B:
    print("B is greater than A")
else:
    print("A and B are equal")