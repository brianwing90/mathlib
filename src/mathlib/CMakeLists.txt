set(MATHLIB_SOURCES
        ${CMAKE_CURRENT_SOURCE_DIR}/math.cpp)

add_library(mathlib SHARED ${MATHLIB_SOURCES})

set_target_properties(mathlib
        PROPERTIES
            PUBLIC_HEADER
                "${MATHLIB_PUBLIC_HEADERS}"
            VERSION
                ${CMAKE_PROJECT_VERSION}
            SOVERSION
                ${CMAKE_PROJECT_VERSION_MAJOR})

install(TARGETS
            mathlib
        LIBRARY DESTINATION
            ${CMAKE_INSTALL_LIBDIR}
        ARCHIVE DESTINATION
            ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER DESTINATION
            ${CMAKE_INSTALL_INCLUDEDIR}/mathlib)

include(CMakePackageConfigHelpers)
configure_package_config_file(
        ${CMAKE_CURRENT_SOURCE_DIR}/MathLibConfig.cmake.in
        ${CMAKE_CURRENT_BINARY_DIR}/MathLibConfig.cmake
        INSTALL_DESTINATION
            ${CMAKE_INSTALL_FULL_DATADIR}/MathLib
        PATH_VARS
            CMAKE_INSTALL_LIBDIR
            CMAKE_INSTALL_INCLUDEDIR)
write_basic_package_version_file(${CMAKE_CURRENT_BINARY_DIR}/MathLibConfigVersion.cmake COMPATIBILITY SameMajorVersion)
install(FILES
            ${CMAKE_CURRENT_BINARY_DIR}/MathLibConfig.cmake
            ${CMAKE_CURRENT_BINARY_DIR}/MathLibConfigVersion.cmake
        DESTINATION
            ${CMAKE_INSTALL_DATADIR}/MathLib)
