#define CATCH_CONFIG_MAIN

#include "catch2/catch.hpp"

#include "mathlib/math.h"


TEST_CASE("1: Test Addition")
{
    REQUIRE(mathlib::add(1,2) == 3);
    REQUIRE(mathlib::add(2,3) == 5);
    REQUIRE(mathlib::add(3,4) == 7);
    REQUIRE(mathlib::add(20,20) == 40);
}

TEST_CASE("2: Test Subtraction")
{
    REQUIRE(mathlib::subtract(2,1) == 1);
    REQUIRE(mathlib::subtract(3,2) == 1);
    REQUIRE(mathlib::subtract(4,3) == 1);
    REQUIRE(mathlib::subtract(20,20) == 0);
}

TEST_CASE("3: Test Factorial")
{
    REQUIRE(mathlib::factorial(3) == 6);
    REQUIRE(mathlib::factorial(4) == 24);
    REQUIRE(mathlib::factorial(5) == 120);
    REQUIRE(mathlib::factorial(10) == 3628800);
}
