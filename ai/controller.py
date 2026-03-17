class LandingController:
    def __init__(self, target_velocity=0):
        self.target_velocity = target_velocity

    def compute_thrust(self, rocket, gravity):
        # Simple proportional controller
        error = rocket.velocity - self.target_velocity

        kp = 500
        thrust = rocket.mass * (gravity - kp * error / 1000)

        return max(0, thrust)