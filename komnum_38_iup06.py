import numpy as np

# Function Decleration
def f(x):
    return 3 * x**5 - 8 * x**4

def f_double_prime(x):
    return 60 * x**3 - 96 * x**2

# Trapezoidal Formula
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    integral = (func(a) + func(b)) / 2
    for i in range(1, n):
        integral += func(a + i * h)
    integral *= h
    return integral

# Integral Calculation
def exact_integral(a, b):
    def F(x):
        return (1/2) * x**6 - (8/5) * x**5
    return F(b) - F(a)

def calculate_trapezoidal_error_bound(a, b, n):
    # Find the maximum of |f''(x)| on the interval [a, b]
    x_values_to_check = [a, b]
    # Critical points of f''(x) (where f'''(x) = 0): 180x^2 - 192x = 0 => 12x(15x - 16) = 0
    # x = 0 or x = 16/15 (~1.067)
    # Check if these are within [a,b]
    if a <= 0 <= b:
        x_values_to_check.append(0)
    if a <= 16/15 <= b:
        x_values_to_check.append(16/15)

    max_f_double_prime = 0
    for x_val in x_values_to_check:
        max_f_double_prime = max(max_f_double_prime, abs(f_double_prime(x_val)))

    # Error formula for Trapezoidal Rule
    error_bound = ((b - a)**3 / (12 * n**2)) * max_f_double_prime
    return error_bound

# Parameters
lower_bound = 4
upper_bound = 16

# --- Calculations ---

# 1. Exact Area
exact_area = exact_integral(lower_bound, upper_bound)
print(f"Exact Area of f(x) from {lower_bound} to {upper_bound}: {exact_area:.6f}\n")

# 2. Trapezoidal Rule Approximation
# Choosing a number of subintervals, for example, n = 10
n_subintervals = 10
approx_area_trapezoidal = trapezoidal_rule(f, lower_bound, upper_bound, n_subintervals)
print(f"Approximation using Trapezoidal Rule (n={n_subintervals}): {approx_area_trapezoidal:.6f}")

# 3. True Error of Trapezoidal Rule Approximation
true_error = abs(exact_area - approx_area_trapezoidal)
print(f"True Error for Trapezoidal Rule (n={n_subintervals}): {true_error:.6f}\n")

# 4. Error Bound Calculation
error_bound_trapezoidal = calculate_trapezoidal_error_bound(lower_bound, upper_bound, n_subintervals)
print(f"Maximum Error Bound for Trapezoidal Rule (n={n_subintervals}): {error_bound_trapezoidal:.6f}")
print(f"(The true error {true_error:.6f} should be less than or equal to the error bound {error_bound_trapezoidal:.6f})\n")

# Trying with a different 'n' to see how the approximation and error change
# For example, let's try with n = 100
print("\n--- Recalculating with n = 100 ---")
n_subintervals_large = 100
approx_area_trapezoidal_large_n = trapezoidal_rule(f, lower_bound, upper_bound, n_subintervals_large)
print(f"Approximation using Trapezoidal Rule (n={n_subintervals_large}): {approx_area_trapezoidal_large_n:.6f}")
true_error_large_n = abs(exact_area - approx_area_trapezoidal_large_n)
print(f"True Error for Trapezoidal Rule (n={n_subintervals_large}): {true_error_large_n:.6f}")
error_bound_trapezoidal_large_n = calculate_trapezoidal_error_bound(lower_bound, upper_bound, n_subintervals_large)
print(f"Maximum Error Bound for Trapezoidal Rule (n={n_subintervals_large}): {error_bound_trapezoidal_large_n:.6f}")