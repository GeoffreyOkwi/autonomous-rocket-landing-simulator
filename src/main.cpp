#include <iostream>

#include "physics.h"
#include "controller.h"
#include "telemetry_writer.h"

int main(int argc, char* argv[])
{
    double gravity = 9.81;

    if (argc > 1)
    {
        gravity = std::stod(argv[1]);
    }
    std::cout << "Gravity set to: " << gravity << std::endl;

    std::cout << "Rocket Simulation Started\n";

    State state;

    state.gravity = gravity;

    state.altitude = 5000.0;
    state.velocity = 2.0;
    state.acceleration = 0.0;
    state.fuel = 1000.0;
    state.throttle = 0.0;

    Physics physics;

    Controller controller(0.6, 0.02, 0.3, true);

    TelemetryWriter telemetry("telemetry.csv");

    telemetry.writeHeader();

    double time = 0.0;
    double dt = 0.01;

    while (state.altitude > 0)
    {
        controller.update(state, dt);

        physics.update(state, dt);

        telemetry.log(
            time,
            state.altitude,
            state.velocity,
            state.acceleration,
            state.fuel,
            state.throttle
        );

        time += dt;
    }

    std::cout << "Simulation Finished\n";

    std::cout << "Final Velocity: " << state.velocity << " m/s\n";

    return 0;
}
