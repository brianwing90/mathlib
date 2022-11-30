cmake_minimum_required(VERSION 3.16)

# Use git to find latest version from tags matching v*.*.*
find_package(Git REQUIRED)
exec_program("git describe --tags --abbrev=0" OUTPUT_VARIABLE VERSION)
string(REGEX MATCH "^[v]?([0-9]+.[0-9]+.[0-9]+)" _ ${VERSION} "v0.0.1")
set(VERSION ${CMAKE_MATCH_1})
if(NOT VERSION)
    set(VERSION "0.0.1")  # Default version.
endif()

project(mathlib VERSION ${VERSION})

message(STATUS "${CMAKE_PROJECT_NAME} version \"${CMAKE_PROJECT_VERSION}\"")

option(BUILD_TESTS "Build unit tests" OFF)

set(CMAKE_CXX_STANDARD 17)

include(GNUInstallDirs)

include_directories(include)

add_subdirectory(include)
add_subdirectory(src)

if(BUILD_TESTS)
    include_directories(external)
    add_subdirectory(tests)
endif()
