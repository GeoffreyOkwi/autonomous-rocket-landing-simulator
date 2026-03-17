#ifndef PHYSICS_H
#define PHYSICS_H

#include "state.h"

class Physics
{
public:
    Physics();

    void update(State& state, double dt);
};

#endif