import numpy as np
import matplotlib.pyplot as plt

class PIDController:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint

        self.prev_error = 0
        self.integral = 0
    
    def compute(self, current_value, dt):
        error = self.setpoint - current_value

        # Proportional
        p = self.kp * error

        # Integral - accumulate error over time
        self.integral += error * dt
        i = self.ki * self.integral

        # Derivative - rate of change of error
        derivative = (error - self.prev_error)/dt
        d = self.kd * derivative

        self.prev_error = error

        return p + i + d
    
# Simulation parameters
dt = 0.01                   # time step in seconds
t = np.arange(0, 10, dt)    # 10 seconds of simulationm time

# PID gains
pid = PIDController(kp = 1.2, ki = 0.5, kd = 0.1, setpoint = 1.0)

# Simulate robot speed
speed = 0.0
speeds = []

for _ in t:
    output = pid.compute(speed, dt)
    speed += output * dt
    speeds.append(speed)

# Plot
plt.figure(figsize = (10, 5))
plt.plot(t, speeds, label = "Robot Speed")
plt.axhline(y = 1.0, color = 'r', linestyle = '--', label = "Setpoint")
plt.xlabel("Time(s)")
plt.ylabel("Speed (m/s)")
plt.title("PID Controller - Speed Tracking")
plt.legend()
plt.grid(True)
plt.show()