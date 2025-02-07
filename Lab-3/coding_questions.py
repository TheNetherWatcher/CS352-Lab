import numpy as np
import matplotlib.pyplot as plt

# Question 1: Array Creation and Indexing
matrix = np.random.rand(4, 4)  
print("Question 1: Unmodified Matrix:\n", matrix)
matrix[:, 0] = 1               
print("Question 1: Modified Matrix:\n", matrix)

A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

add = A + B
subtract = A - B
multiply = A * B
divide = A / B

print("Question 2: Addition:\n", add)
print("Question 2: Subtraction:\n", subtract)
print("Question 2: Multiplication:\n", multiply)
print("Question 2: Division:\n", divide)

print("Determinant of A:", np.linalg.det(A))
print("Determinant of B:", np.linalg.det(B))

# Question 3: Broadcasting in NumPy
matrix = np.random.randint(1, 10, (3, 3))
array = np.array([1, 2, 3])
result = matrix + array  # Broadcasting
print("Question 3: Broadcasting Result:\n", result)

# Question 4: Midpoint Theorem
def calculate_midpoint(x1, y1, x2, y2):
    Mx = (x1 + x2) / 2
    My = (y1 + y2) / 2
    return Mx, My

midpoint = calculate_midpoint(2, 3, 4, 7)
print("Question 4: Midpoint:", midpoint)

# Question 5: Plotting with Matplotlib
x = np.linspace(0, 2 * np.pi, 10000)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure()
plt.plot(x, y_sin, 'r--', label='sin(x)')  
plt.plot(x, y_cos, 'b-', label='cos(x)')   # Blue solid line with triangles
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Question 5: Sine and Cosine Functions')
plt.legend()
plt.show()

# Question 6: Bresenham’s Line Drawing Algorithm
def bresenham(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points

line_points = bresenham(2, 2, 10, 8)
print("Question 6: Line Points:", line_points)

# Plotting the line
x_coords, y_coords = zip(*line_points)
plt.figure()
plt.plot(x_coords, y_coords, marker='o')
plt.title("Question 6: Bresenham's Line Drawing Algorithm")
plt.grid(True)
plt.show()
