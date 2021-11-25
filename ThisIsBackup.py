# This is purely for backup
import numpy as np


class FRG:  # Farest range get
    def __init__(self, speed, height):
        self.speed = speed
        self.height = height

    @staticmethod
    def air_c():
        m = 0.1
        r = 0.2
        rho = 1.2
        Cd = 0.5
        A = np.pi*r**2
        DeltaAC = 0.5*Cd*rho*A/m
        return DeltaAC

    def getRange(self, angleR, dt):
        theta = np.radians(angleR)
        vx0 = self.speed*np.cos(theta)
        vy0 = self.speed*np.sin(theta)
        r2 = np.array([0., 0.])
        v2 = np.array([vx0, vy0])
        print(self)
        a2 = np.array([0., 9.8])-self.air_c()*v2
        # t = 0.
        x2 = []
        y2 = []
        while True:
            if(r2[1] < -self.height):
                break
            # print('%10.4f'*3 % (t, r2[0], r2[1]))
            x2.append(r2[0])
            y2.append(r2[1]+self.height)
            a2 = np.array([0., 9.8])-self.air_c()*v2
            v2 += a2*dt
            r2 += v2*dt
            # t += dt
        return np.array([x2, y2])

    def AccurateAngle(self, begin, end, count):
        mid = self.a((begin+end)/2)
        if(count > 20):
            return mid.deg
        nextMid = self.a(mid.deg+0.01)
        if (nextMid.distance > mid.distance):
            self.AccurateAngle(mid, end, count+1)
            print(nextMid.deg)
        else:
            self.AccurateAngle(begin, mid, count+1)
    def a(self, deg):
            self.deg = deg
            self.distance = self.getRange(deg, 0.01)[0][-1]
# class lazyGR(FRG):
#     def __init__(self, deg):
#         super().__init__()
#         self.deg = deg
#         self.distance = self.getRange(deg, 0.01)[0][-1]


    
