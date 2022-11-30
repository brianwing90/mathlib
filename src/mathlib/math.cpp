#include "mathlib/math.h"

namespace mathlib {

int add(int num1, int num2)
{
    return num1 + num2;
}

int subtract(int num1, int num2)
{
    return num1 - num2;
}

int factorial(int num)
{
    return num <= 1 ? 1 : factorial(num - 1) * num;
}

}
