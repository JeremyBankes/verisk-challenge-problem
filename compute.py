# Jeremy Bankes - jeremy.bankes@gmail.com - July 31, 2024
# Tested for Python 3.6.9

# Notes to the reviewer:
# - I used the style guide outlined here: https://peps.python.org/pep-0008/
# - I broke the important formulas for applying the threshold & limits into
#   their own functions to make it easy to view and/or change their behavior
#   independent of the rest of the implementation.
# - I assume valid user input. (No error handling)

import sys

def apply_threshold_modifications(
        input_value: float, threshold: float) -> float:
    return max(0.0, input_value - threshold)

def apply_limit_modifications(
        input_value: float, current_sum: float, limit: float) -> float:
     return min(limit - current_sum, input_value)

# Parse command-lind arguments.
_, threshold, limit = sys.argv
threshold = float(threshold)
limit = float(limit)

# Parse input lines from standard in.
inputs = []
for line in sys.stdin:
    inputs.append(float(line.strip()))

# Crunch numbers
current_sum = 0.0
for input_value in inputs:
    output = apply_threshold_modifications(input_value, threshold)
    output = apply_limit_modifications(output, current_sum, limit)
    current_sum += output
    print(output)
print(current_sum)
