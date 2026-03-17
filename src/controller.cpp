#include "controller.h"

Controller::Controller(double kp, double ki, double kd, bool autopilot)
{
    this->kp = kp;
    this->ki = ki;
    this->kd = kd;

    this->autopilot = autopilot;

    integral = 0;
    prev_error = 0;
}

void Controller::update(State& state, double dt)
{
    if (!autopilot)
        return;

    double target_velocity = -2.0;

    double error = target_velocity - state.velocity;

    integral += error * dt;

    double derivative = (error - prev_error) / dt;

    double output = kp * error + ki * integral + kd * derivative;

    prev_error = error;

    if (output < 0)
        output = 0;

    if (output > 1)
        output = 1;

    state.throttle = output;
}