from matplotlib import colors, legend
import matplotlib.pyplot as plt
from matplotlib import widgets as wid
import numpy as np
import matplotlib.gridspec as gridspec
from menu import Menu,MenuItem,ItemProperties
# from matplotlib.animation import FuncAnimation as mata
# import drawImage as drim
# from PIL import Image as ima
# import matplotlib.image as mpimg
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.595, left=0.045, right=0.971, top=1)

plt.axhline(color="black", label="_nolegend_")
plt.axvline(color="black", label="_nolegend_")
# t = np.arange(-10.0, 10.0, 0.001)
# y = np.cos(t)
# l, = ax.plot(t, y, lw=2, label='Fuck this cos')
speedI = fig.add_axes([0.05, 0.45, 0.1, 0.05])
TB_spe = wid.TextBox(speedI, "Speed", initial='60')
HeightI = fig.add_axes([0.18, 0.45, 0.1, 0.05])
TB_hei = wid.TextBox(HeightI, "Height", initial='0')
SubmitI = fig.add_axes([0.40, 0.05, 0.1, 0.05])
Btn_sub = wid.Button(SubmitI, "Submit")
fig.canvas.manager.set_window_title('Test')
m = 0.1
r = 0.2
rho = 1.2
Cd = 0.5
g = -9.8
height = 100.
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
    print('%10.4f'*3 % (t, r2[0], r2[1]))
    x2.append(r2[0])
    y2.append(r2[1]+100)
    a2 = np.array([0., g])-air_c*v2
    v2 += a2*dt
    r2 += v2*dt
    t += dt
line, = ax.plot(x2, y2, 'b-')


def submit(event):
    m = 0.1
    r = 0.2
    rho = 1.2922
    Cd = 0.5
    g = -9.8
    degree = 60.0
    A = np.pi*r**2
    air_c = 0.5*Cd*rho*A/m
    TB_speV = 60. if (TB_spe.text == "") else float(TB_spe.text)
    v0 = float(TB_speV)
    TB_heiV = 0. if (TB_hei.text == "") else float(TB_hei.text)
    theta = np.radians(degree)
    vx0 = v0*np.cos(theta)
    vy0 = v0*np.sin(theta)
    r2 = np.array([0., 0.])
    v2 = np.array([vx0, vy0])
    a2 = np.array([0., g])-air_c*v2
    t, dt = 0., 0.01
    x2 = []
    y2 = []

    while True:
        if(r2[1] < -TB_heiV):
            break
        print('%10.4f'*3 % (t, r2[0], r2[1]))
        x2.append(r2[0])
        y2.append(r2[1]+TB_heiV)
        a2 = np.array([0., g])-air_c*v2
        v2 += a2*dt
        r2 += v2*dt
        t += dt
    line.set_xdata(x2)
    line.set_ydata(y2)
    ax.relim()
    ax.autoscale_view()
    plt.draw()


# ax.legend([line], [""], handler_map={
#     line: drim.HandlerLineImage("C:\\Users\Ryan\Desktop\Output For Blender\poster_fix_title_1.png")},
#     handlelength=2, labelspacing=0.0, fontsize=72, borderpad=0.15, loc=2,
#     handletextpad=0.2, borderaxespad=0.45)
Btn_sub.on_clicked(submit)
fig.set_size_inches(10.5, 9.5, forward=True)
plt.show()
