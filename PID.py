import matplotlib.pyplot as plt

class PID:
    def __init__(self, kP, kI, kD, maxError = None):
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.maxError = maxError
        self.error = 0
        self.prevError = 0
        self.integral = 0
        self.derivative = 0
        self.output = 0

    def step(self, error, dt):
        self.error = error
        self.derivative = (self.error - self.prevError) / dt
        self.integral += self.error * dt
        self.prevError = self.error

        self.output = self.kP * self.error + self.kI * self.integral + self.kD * self.derivative 
        return self.output

    def getError(self):
        return self.error

    def isSettled(self):
        return self.error < self.maxError