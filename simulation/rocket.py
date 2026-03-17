class Rocket:
    def __init__(self, mass=1000.0, thrust=15000.0, altitude=0.0, velocity=0.0):
        self.mass = mass
        self.thrust = thrust
        self.velocity = velocity
        self.altitude = altitude

    def update(self, dt, gravity=9.81):
        acceleration = (self.thrust / self.mass) - gravity
        self.velocity += acceleration * dt
        self.altitude += self.velocity * dt

        return self.altitude, self.velocity