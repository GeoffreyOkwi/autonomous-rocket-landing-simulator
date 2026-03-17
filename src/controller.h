#ifndef CONTROLLER_H
#define CONTROLLER_H

#include "state.h"

class Controller
{
public:
    Controller(double kp, double ki, double kd, bool autopilot);

    void update(State& state, double dt);

private:
    double kp;
    double ki;
    double kd;

    double integral;
    double prev_error;

    bool autopilot;
};

#endif