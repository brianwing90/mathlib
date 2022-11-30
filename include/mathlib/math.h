#ifndef MATHLIB_MATH_H
#define MATHLIB_MATH_H

namespace mathlib {

/**
 * Returns the sum of the two given integers.
 *
 * @param num1 The value to add to num2.
 * @param num2 The value to add to num1.
 * @return The sum of num1 + num2
 */
int add(int num1, int num2);

/**
 * Returns the difference of the two given integers.
 *
 * @param num1 The value to subtract from num2.
 * @param num2 The value to subtract from num1.
 * @return The difference of num1 - num2
 */
int subtract(int num1, int num2);

/**
 * Returns the product of the given integer and all whole numbers from it to 0, not inclusive.
 *
 * Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
 *
 * @param num The value to start from.
 * @return The factorial of the given integer.
 */
int factorial(int num);

}

#endif // MATHLIB_MATH_H
