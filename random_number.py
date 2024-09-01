"""In Python, there are several methods to generate random numbers, but the most common counterpart to random.randint() is random.random().

1. random.randint(a, b)
Description: Generates a random integer between a and b (both inclusive).

Example:      """

# import random

# random_number = random.randint(1, 10)  # Returns an integer between 1 and 10
# print(random_number)


"""2. random.random()
Description: Generates a random floating-point number between 0.0 and 1.0 (0.0 inclusive, 1.0 exclusive).

Example:      """

# import random

# random_float = random.random()  # Returns a float between 0.0 and 1.0
# print(random_float)


""" Differences:
random.randint(a, b): Used when you need a random integer within a specific range.
random.random(): Used when you need a random floating-point number between 0 and 1.
    Use Cases:
random.randint(): Ideal for scenarios like rolling a dice, selecting a random index, or generating an integer within a range.
random.random(): Often used in scenarios requiring random probability or when scaling to a different range is needed by multiplying the result.
    Scaling random.random() to a Range:
You can scale the result of random.random() to generate a float in a different range, say between a and b:

    Example:      """

# import random

# a = 5
# b = 10
# random_float_in_range = a + (b - a) * random.random()
# print(random_float_in_range)  # Returns a float between 5 and 10


"""This will give you a random floating-point number between a and b."""

"""Example in Detail:

Let's consider the specific case where a = 5 and b = 10:

Step 1: Calculate b - a:

b - a = 10 - 5 = 5

Step 2: Generate a random number between 0.0 and 1.0 using random.random(). Suppose it generates 0.7.

Step 3: Multiply 0.7 by 5 (which is b - a):

0.7 * 5 = 3.5

Step 4: Add a to shift the result:

3.5 + 5=8.5

Thus, 8.5 is a random float within the range [5, 10).

Conclusion:
    The expression a + (b - a) ensures that the random float is correctly scaled to the interval [a, b).

    b - a scales the result to the correct width, and a shifts the range to start from a instead of 0.      """

"""DO MORE LEARN MORE"""