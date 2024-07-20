import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import sympy as sp

# Function to safely evaluate user input
def evaluate_function(expr, x):
    f = sp.lambdify(x, expr, 'numpy')
    return f

# Get user input for the 2D curve function
curve_input = input("Enter the 2D curve function in terms of x (e.g., sin(x), x**2): ")
x = sp.symbols('x')
curve_expr = sp.sympify(curve_input)
curve_function = evaluate_function(curve_expr, x)

# Get user input for the axis of revolution
axis_of_revolution = input("Enter the axis of revolution ('x' or 'y'): ").strip().lower()

# Get user input for the range of x
x_min = float(input("Enter the minimum value of x: "))
x_max = float(input("Enter the maximum value of x: "))

# Calculate the volume of the solid of revolution
def integrand(x):
    return np.pi * (curve_function(x))**2

volume, _ = quad(integrand, x_min, x_max)
print(f"Volume of the solid of revolution: {volume}")

# Plot the 2D curve and the solid of revolution
x_vals = np.linspace(x_min, x_max, 100)
y_vals = curve_function(x_vals)

fig = plt.figure(figsize=(12, 6))

# Plot the 2D curve
ax1 = fig.add_subplot(121)
ax1.plot(x_vals, y_vals, label=f'y = {curve_input}')
ax1.fill_between(x_vals, 0, y_vals, alpha=0.2)
ax1.set_title("2D Curve")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()

# Plot the solid of revolution
ax2 = fig.add_subplot(122, projection='3d')
theta = np.linspace(0, 2 * np.pi, 100)
X, Theta = np.meshgrid(x_vals, theta)

if axis_of_revolution == 'x':
    Y = curve_function(X)
    Z = Y * np.sin(Theta)
    Y = Y * np.cos(Theta)
    ax2.set_title("Solid of Revolution (about x-axis)")
else:  # Revolving about the y-axis
    Y = X
    X = curve_function(X)
    Z = X * np.sin(Theta)
    X = X * np.cos(Theta)
    ax2.set_title("Solid of Revolution (about y-axis)")

ax2.plot_surface(X, Y, Z, rstride=5, cstride=5, color='b', alpha=0.6)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("z")

plt.show()
