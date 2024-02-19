def rotate_array(arr, direction):
    if direction == 'left':
        return [list(row)[::-1] for row in zip(*arr)][::-1]
    elif direction == 'right':
        return [list(row) for row in zip(*arr[::-1])]
    else:
        raise ValueError("Invalid direction. Please provide 'left' or 'right'.")

# Test the function
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print("Original array:")
for row in arr:
    print(row)

print("\nRotated 90 degrees counterclockwise:")
rotated_left = rotate_array(arr, 'left')
for row in rotated_left:
    print(row)

print("\nRotated 90 degrees clockwise:")
rotated_right = rotate_array(arr, 'right')
for row in rotated_right:
    print(row)