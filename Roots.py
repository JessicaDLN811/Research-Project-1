import numpy as np

# Functions
def f1(x): return x**3 - 5*x**2 + 2*x
def f2(x): return x**3 - 2*x**2 - 5
def df1(x): return 3*x**2 - 10*x + 2
def df2(x): return 3*x**2 - 4*x

# Utility: format results
def print_table(name, iters):
    print(f"\n{name} Method")
    print("Iter | x_n        | Error")
    print("-------------------------------")
    for i in range(len(iters)):
        if i == 0:
            print(f"{i:>4} | {iters[i]:<10.6f} |    -")
        else:
            err = abs(iters[i] - iters[i-1])
            print(f"{i:>4} | {iters[i]:<10.6f} | {err:.6e}")
    print(f"Final Approx: {iters[-1]:.6f}\n")

# Bisection
def bisection(f, a, b, tol=1e-4):
    iters = []
    while (b-a)/2 > tol:
        c = (a+b)/2
        iters.append(c)
        if f(c) == 0: break
        elif f(a)*f(c) < 0: b = c
        else: a = c
    return iters

# Newton
def newton(f, df, x0, tol=1e-4):
    iters = [x0]
    while True:
        x1 = x0 - f(x0)/df(x0)
        iters.append(x1)
        if abs(x1-x0) < tol: break
        x0 = x1
    return iters

# Secant
def secant(f, x0, x1, tol=1e-4):
    iters = [x0, x1]
    while True:
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        iters.append(x2)
        if abs(x2-x1) < tol: break
        x0, x1 = x1, x2
    return iters

# Muller
def muller(f, x0, x1, x2, tol=1e-4, max_iter=100):
    iters = [x0, x1, x2]
    for _ in range(max_iter):
        h1, h2 = x1 - x0, x2 - x1
        d1, d2 = (f(x1) - f(x0)) / h1, (f(x2) - f(x1)) / h2
        a = (d2 - d1) / (h2 + h1)
        b = a*h2 + d2
        c = f(x2)

        # Compute discriminant safely (allow complex)
        rad = np.sqrt(b**2 - 4*a*c + 0j)

        # Choose denominator with larger magnitude
        den1, den2 = b + rad, b - rad
        den = den1 if abs(den1) > abs(den2) else den2

        # Check for zero denominator
        if den == 0:
            print("Warning: zero denominator encountered in Muller")
            break

        dxr = -2 * c / den
        x3 = x2 + dxr
        iters.append(x3)

        if abs(dxr) < tol:
            break

        x0, x1, x2 = x1, x2, x3

    return iters
# === Run & Print Tables ===
if __name__ == "__main__":
    print("\n=== Problem (a): f(x) = x^3 - 5x^2 + 2x ===")
    print_table("Bisection f1", bisection(f1, 0, 1))
    print_table("Newton f1", newton(f1, df1, 0.5))
    print_table("Secant f1", secant(f1, 0.2, 0.7))
    print_table("Muller f1", muller(f1, 0, 1, 2))

    print("\n=== Problem (b): f(x) = x^3 - 2x^2 - 5 ===")
    print_table("Bisection f2", bisection(f2, 2, 3))
    print_table("Newton f2", newton(f2, df2, 2.5))
    print_table("Secant f2", secant(f2, 2, 3))
    print_table("Muller f2", muller(f2, 1, 2, 3))
    
    
    import matplotlib.pyplot as plt

def compute_errors(iters):
    """Compute successive errors |x_{n+1} - x_n|"""
    return [abs(iters[i+1]-iters[i]) for i in range(len(iters)-1)]

def plot_all_methods(f, df, a, b, x0, x1, x2, title):
    # Collect iterations
    bisection_iters = bisection(f, a, b)
    newton_iters    = newton(f, df, x0)
    secant_iters    = secant(f, x0, x1)
    muller_iters    = muller(f, a, x0, x1)

    # Compute errors
    methods = {
        "Bisection": compute_errors(bisection_iters),
        "Newton": compute_errors(newton_iters),
        "Secant": compute_errors(secant_iters),
        "Muller": compute_errors(muller_iters)
    }

    # Plot
    plt.figure()
    for name, errors in methods.items():
        plt.semilogy(range(1, len(errors)+1), errors, marker='o', label=name)

    plt.xlabel("Iteration")
    plt.ylabel("Error (log scale)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example calls:
plot_all_methods(f1, df1, 0, 1, 0.5, 0.7, 2, "Error Convergence for f1 = x^3 - 5x^2 + 2x")
plot_all_methods(f2, df2, 2, 3, 2.5, 3, 1, "Error Convergence for f2 = x^3 - 2x^2 - 5")
