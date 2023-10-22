def newton_raphson(f, x0, tolerance, max_iterations):
    steps_text = "\nNewton-Raphson Steps of Iteration:\n\n"
    steps_text += "N\t Xn\t F(Xn)\n\n"
    for i in range(max_iterations):
        fx = f(x0)
        if abs(fx) < tolerance:
            return x0, abs(fx), "Number of iterations: {}".format(i), steps_text
        dfx = (f(x0 + tolerance) - fx) / tolerance  # Approximate the derivative
        if dfx == 0:
            error_msg = "The derivative is zero."
            steps_text += error_msg
            return None, None, error_msg, steps_text
        x0 = x0 - fx / dfx
        steps_text += f"{i+1}\t {x0:.3f}\t {abs(f(x0)):.3f}\n"
    error_msg = "The method failed after {} iterations.".format(max_iterations)
    return x0, abs(f(x0)), "the method failed after {} iterations.".format(max_iterations), steps_text
