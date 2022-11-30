set(TEST_SOURCES
        ${CMAKE_CURRENT_SOURCE_DIR}/test_mathlib.cpp
        )

add_executable(test_mathlib ${TEST_SOURCES})
target_link_libraries(test_mathlib PRIVATE mathlib)
