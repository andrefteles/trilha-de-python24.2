# b) Conseguem resolver meu exercício de cálculo 4?? Vocês tem que avaliar,
# com loops que a gente já aprendeu, se essa série, somando “todos” os
# termos vai ou não vai convergir para um valor.

import math

def series_term(n):
    """Calculate the nth term of the series 1 / (n * ln^2(n))."""
    if n > 1:
        return 1 / (n * (math.log(n)) ** 2)
    return 0

def check_convergence(threshold=1e-6, max_iterations=1000000):
    """Sum the series and stop when the difference between terms is less than the threshold."""
    n = 2  # Start from n=2
    sum_series = 0
    prev_sum = 0  # To track the previous sum value
    iterations = 0

    while iterations < max_iterations:
        term = series_term(n)
        sum_series += term
        
        # Calculate the difference between the current and previous sum
        difference = abs(sum_series - prev_sum)
        
        # Print the current value of n, the term, and the sum
        print(f"n={n}, term={term}, sum={sum_series}, difference={difference}")
        
        # Check if the change in sum is less than the threshold
        if difference < threshold:
            print("\nThe series seems to converge.")
            break
        
        # Update values for the next iteration
        prev_sum = sum_series
        n += 1
        iterations += 1
    
    if iterations == max_iterations:
        print(f"Reached the maximum number of iterations ({max_iterations}).")
    
    return sum_series

# Run the convergence check
final_sum = check_convergence()
print(f"\nFinal sum of the series: {final_sum}\n")
