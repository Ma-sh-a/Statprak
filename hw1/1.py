#make tuple
num_tuple = tuple(x for x in range(int(12345**0.5)+1) if x**2 % 3 == 0 and x**2 % 4 == 0 and x**2 % 8 != 0 and x**2 < 12345)

print(num_tuple)