import numpy as np


class Ball:
    def __init__(self, speed, height):
        self.speed = speed
        self.height = height
        self.m = 1
        self.r = 0.2
        self.rho = 1.2
        self.Cd = 0.5
        self.A = np.pi * self.r ** 2
        self.air_c = 0.5*self.Cd*self.rho*self.A/self.m

    def distanceWithAir(self, degree, dTime=0.01):
        G = 9.8
        x = 0
        y = self.height
        vx = np.cos(degree * np.pi / 180) * self.speed
        vy = np.sin(degree * np.pi / 180) * self.speed
        while (y >= 0):  # 計算投擲距離
            cx = -vx * (self.air_c / self.m)
            cy = -vy * (self.air_c / self.m) - G
            vx = vx + cx * dTime
            vy = vy + cy * dTime
            dx = (vx * dTime)
            dy = (vy * dTime) - (0.5 * G * pow(dTime, 2))
            x += dx
            y += dy
        ny = y + dy
        yPercent = ny / vy
        x -= vx * yPercent
        return x

    def distanceWithDeg(self, degree, dTime=0.01):
        G = 9.8
        x = 0
        y = self.height
        x2 = []
        y2 = []
        theta = np.radians(degree)
        vx = np.cos(theta) * self.speed
        vy = np.sin(theta) * self.speed
        while (y >= 0):  # 計算投擲距離
            cx = -vx * (self.air_c / self.m)
            cy = -vy * (self.air_c / self.m) - G
            vx = vx + cx * dTime
            vy = vy + cy * dTime
            dx = (vx * dTime)
            dy = (vy * dTime) - (0.5 * G * pow(dTime, 2))
            x += dx
            y += dy
            x2.append(x)
            y2.append(y)
        ny = y + dy
        yPercent = ny / vy
        x -= vx * yPercent
        x2[-1] = x
        r2 = np.array([x2, y2])
        return r2

    def preciseAngle(self, lowest, highest, count):
        mid = (lowest+highest)/2
        midD = self.distanceWithAir(mid, 0.001)
        if count > 20:
            return np.array([mid, midD])
        Nextmid = mid + 0.001
        NextmidD = self.distanceWithAir(Nextmid, 0.001)
        if NextmidD > midD:
            return self.preciseAngle(Nextmid, highest, count+1)
        else:
            return self.preciseAngle(lowest, mid, count+1)
