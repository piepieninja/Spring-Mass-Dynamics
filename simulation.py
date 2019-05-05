# ========================#
#                         #
# Author: Caleb Adams     #
# http://calebadams.space #
# Spring Mass Dynamics    #
#                         #
# ========================#
#
# This simulation's matplotlib backend
# is mostly followed from this double
# pendulum example https://matplotlib.org/gallery/animation/double_pendulum_sgskip.html
#

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np
import sys

# ============== #
# system globals #
# ============== #

# initila displacement
x = 0.7
# restoring force from initial displacement
N = 25.6
# spring constant
k = -1 * (N/x)
# mass
m = 2.0
# stepsize
h = 0.5
# default max_t
max_t = 30

# ============ #
# matrix terms #
# ============ #

# the tridiagonal terms in A
a = (1/h**2)
b = (-2/h**2) - (k/m)
c = (1/h**2)
A = []
X = []
B = []

# matplotlib intializations
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1, 5), ylim=(-1, 5))
ax.set_aspect('equal')
ax.grid()

# line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(h, 0.9, '', transform=ax.transAxes)

wave, = ax.plot([], [], '-', lw=2)

rect = patches.Rectangle((2,-0.75),1.5,1.5,linewidth=1,edgecolor='#33ccff',facecolor='#33ccff')
# ax.add_patch(rect)

def printA(M):
    global A
    for x in range(0,M):
        line = ""
        for y in range(0,M):
            # print A[x][y]
            line += str(int(A[x][y])) + " "
        print line
#
# generates the A matrix
# of size MxM
def generateA(M):
    global A
    row_count = 0
    for x in range(0,M):
        new_row = np.zeros(M)
        if (row_count == 0):
            new_row[0] = b
            new_row[1] = c
        elif (row_count == M-1):
            new_row[max_t-2] = a
            new_row[max_t-1] = b
        else:
            new_row[x-1] = a
            new_row[x]   = b
            new_row[x+1] = c
        row_count += 1
        A.append(new_row)

def reset_abc():
    global a,b,c
    a = (1/h**2)
    b = (-2/h**2) - (k/m)
    c = (1/h**2)

#
# generates the B vector
#
def generateB(M):
    global B
    B = np.zeros(M)
    x_init = x
    # during the first thing
    B[0] = -1 * a*(x_init)


# a gauss_seidel helper methods
def get_x0(x_1, x_2):
    return (-b * x_1 - c * x_2)/a

def get_x1(x_0, x_2):
    return (-a * x_0 - c * x_2)/b

def get_x2(x_0, x_1):
    return (-a * x_0 - b * x_1)/c

#
# solve for the X vector
# using gauss seidel
#
def gauss_seidel(M):
    global X
    X = np.zeros(M) # initial guess
    X[0] = x
    for gs in range(0,100): # just to run thru gauss_seidel for a bit
        for itr in range(0,M-1):
            if (itr == 0):
                X[itr] = get_x0(X[itr+1],X[itr]+2)
            elif(itr == M-1):
                X[itr] = get_x2(X[itr-2],X[itr-1])
            else:
                X[itr] = get_x1(X[itr-1],X[itr+1])


# housekeeping for animation
def init():
    global X,wave
    # make the intial sine wave
    # ax.plot(6*sin_y),
    wave.set_data([],[])
    ax.add_patch(rect)
    time_text.set_text('')
    return wave, rect, time_text

# housekeeping for animation
def animate(i):
    # print i
    global X,wave
    sin_x = np.arange(-1,X[i],0.001)   # start,stop,step
    sin_y = np.sin((12*abs(-1 - X[i]))*sin_x)
    wave.set_data(sin_x,sin_y)
    rect.set_xy([X[i], -0.75])
    time_text.set_text(time_template % (i*h))
    return wave, rect, time_text


# ============
# entry point
print '#====================================#'
print '#                                    #'
print '#       Spring Mass Simulation       #'
print '#          by: Caleb Adams           #'
print '#                                    #'
print '#====================================#'
print ''
# print '>> what t value would you like to calculate to (100 is plenty)?'

# max_t = int(raw_input(">> what t value would you like to calculate to (15 is plenty)?\n>> "))
# h = float(raw_input(">> what should the h value be (between 0.2 and 0.5 is best)?\n>> "))
max_t = 30
h = 0.5
reset_abc()

gauss_seidel(int(max_t/h))

ani = animation.FuncAnimation(fig, animate, frames=len(X), interval=70, init_func=init)
# ani.save('animation.gif', writer='imagemagick', fps=15)

plt.show()
