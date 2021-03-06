from matplotlib import colors, legend
import matplotlib.pyplot as plt
from matplotlib import widgets as wid
import numpy as np
import matplotlib.gridspec as gridspec
from menu import Menu, MenuItem, ItemProperties
import re
from classes import Ball
# from matplotlib.animation import FuncAnimation as mata
# import drawImage as drim
# from PIL import Image as ima
# import matplotlib.image as mpimg
fig, ax = plt.subplots(2, 1)
fig.subplots_adjust(bottom=0.19, left=0.045, right=0.971, top=1)

plt.axhline(color="black", label="_nolegend_")
plt.axvline(color="black", label="_nolegend_")
# t = np.arange(-10.0, 10.0, 0.001)
# y = np.cos(t)
# l, = ax.plot(t, y, lw=2, label='Fuck this cos')
speedI = fig.add_axes([0.05, 0.05, 0.1, 0.05])
TB_spe = wid.TextBox(speedI, "Speed", initial='60')
HeightI = fig.add_axes([0.18, 0.05, 0.1, 0.05])
TB_hei = wid.TextBox(HeightI, "Height", initial='0')
SubmitI = fig.add_axes([0.40, 0.05, 0.1, 0.05])
Btn_sub = wid.Button(SubmitI, "Submit")
fig.canvas.manager.set_window_title('Test')
m = 1
r = 0.2
rho = 1.2
Cd = 0.5
g = -9.8
height = 0.
A = np.pi*r**2
air_c = 0.5*Cd*rho*A/m
degree = 60.0
theta = np.radians(degree)
v0 = 60.0
vx0 = v0*np.cos(theta)
vy0 = v0*np.sin(theta)
r2 = np.array([0., 0.])
v2 = np.array([vx0, vy0])
a2 = np.array([0., g])-air_c*v2
t, dt = 0., 0.01
x2 = []
y2 = []
while True:
    if(r2[1] < -height):
        break
    # print('%10.4f'*3 % (t, r2[0], r2[1]))
    x2.append(r2[0])
    y2.append(r2[1])
    a2 = np.array([0., g])-air_c*v2
    v2 += a2*dt
    r2 += v2*dt
    t += dt
lineax, = ax[0].plot(x2, y2, 'r-')
lineqte, = ax[1].plot(x2, y2, 'b-')
ax[0].set_xlabel("Angle and Distance")
ax[1].set_xlabel('Farest range with air drag')


def submit(event):
    speed = 60. if (TB_spe.text == "") else float(TB_spe.text)
    height = 0. if (TB_hei.text == "") else float(TB_hei.text)
    lis = []
    ball = Ball(speed, height)
    for x in range(91):
        lis.append(ball.distanceWithAir(x, 0.001))
    y = np.arange(0, 91)
    lineax.set_xdata(y)
    lineax.set_ydata(lis)
    maxval = ball.preciseAngle(0., 90., 0)
    lismax = ball.distanceWithDeg(maxval[0])
    lineqte.set_xdata(lismax[0])
    lineqte.set_ydata(lismax[1])
    ax[0].relim()
    ax[0].autoscale_view()
    ax[1].relim()
    ax[1].autoscale_view()
    ax[0].set_xlabel("Angle and Distance, highest angle: {0:.8f}".format(float(maxval[0])))
    ax[1].set_xlabel('Farest range with air drag, farest range: {0:.8f}'.format(float(maxval[1])))
    plt.draw()
# ax.legend([line], [""], handler_map={
#     line: drim.HandlerLineImage("C:\\Users\Ryan\Desktop\Output For Blender\poster_fix_title_1.png")},
#     handlelength=2, labelspacing=0.0, fontsize=72, borderpad=0.15, loc=2,
#     handletextpad=0.2, borderaxespad=0.45)
Btn_sub.on_clicked(submit)
fig.set_size_inches(10.5, 5.5, forward=True)
plt.show()
