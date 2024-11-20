# Algebra originated in ancient civilizations such as Babylonia.
# It involves solving equations and studying structures such as numbers and symbols.
# Al-Khwarizmi, a Persian mathematician, formalized algebra in the 9th century.

# Solving a quadratic equation: ax^2 + bx + c = 0
import cmath  # For handling complex numbers in case the roots are imaginary

# Coefficients of the equation x^2 - 7x + 10 = 0
a, b, c = 1, -7, 10

# Discriminant (b^2 - 4ac) determines the nature of the roots
discriminant = cmath.sqrt(b**2 - 4*a*c)

# Calculating the two roots of the equation
root1 = (-b + discriminant) / (2 * a)
root2 = (-b - discriminant) / (2 * a)

# Printing the roots
print("Roots of the quadratic equation are:", root1, "and", root2)
