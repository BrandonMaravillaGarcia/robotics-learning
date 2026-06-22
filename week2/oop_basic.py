class Robot:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.current_speed = 0

    def accelerate(self, amount):
        self.current_speed += amount
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        print(f"{self.name} speed: {self.current_speed} m/s")

    def stop(self):
        self.current_speed = 0
        print(f"{self.name} stopped.")

mower = Robot("Robomower", max_speed = 2)
arm = Robot("Roboarm", max_speed = 1)

mower.accelerate(1)
mower.accelerate(1)
mower.accelerate(1)
arm.accelerate(0.5)
mower.stop()

class AutonomousRobot(Robot):
    def __init__(self, name, max_speed, sensor_range):
        super().__init__(name, max_speed)