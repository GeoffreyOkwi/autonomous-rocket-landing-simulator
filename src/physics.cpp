#include "physics.h"

Physics::Physics()
{
}

void Physics::update(State& state, double dt)
{
    double gravity = -state.gravity;

    double thrust = state.throttle * 30.0;

    state.acceleration = gravity + thrust;

    state.velocity += state.acceleration * dt;

    state.altitude += state.velocity * dt;

    if (state.altitude < 0)
        state.altitude = 0;

    state.fuel -= state.throttle * 5.0 * dt;

    if (state.fuel < 0)
        state.fuel = 0;
}