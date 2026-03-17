#ifndef ROCKET_STATE_H
#define ROCKET_STATE_H

struct RocketState {
    double altitude;
    double velocity;
    double acceleration;
    double fuel;
    double throttle;
    double gravity;
};

#endif