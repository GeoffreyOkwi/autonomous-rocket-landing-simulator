cmake_minimum_required(VERSION 3.20)
project(rocket_sim)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(rocket_sim
        src/main.cpp
        src/physics.cpp
        src/telemetry_writer.cpp
        src/controller.cpp
)