# Install script for directory: /home/axle/Dropbox/Semester 8/EE 708/project/EE-708-GNU-Radio-Project/gr-gaussian_code/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gaussian_code" TYPE FILE FILES
    "/home/axle/Dropbox/Semester 8/EE 708/project/EE-708-GNU-Radio-Project/gr-gaussian_code/python/__init__.py"
    "/home/axle/Dropbox/Semester 8/EE 708/project/EE-708-GNU-Radio-Project/gr-gaussian_code/python/gaussian_code_if.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gaussian_code" TYPE FILE FILES
    "/home/axle/Dropbox/Semester 8/EE 708/project/EE-708-GNU-Radio-Project/gr-gaussian_code/build/python/__init__.pyc"
    "/home/axle/Dropbox/Semester 8/EE 708/project/EE-708-GNU-Radio-Project/gr-gaussian_code/build/python/gaussian_code_if.pyc"
    "/home/axle/Dropbox/Semester 8/EE 708/project/EE-708-GNU-Radio-Project/gr-gaussian_code/build/python/__init__.pyo"
    "/home/axle/Dropbox/Semester 8/EE 708/project/EE-708-GNU-Radio-Project/gr-gaussian_code/build/python/gaussian_code_if.pyo"
    )
endif()

