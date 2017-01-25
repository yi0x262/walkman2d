#!/usr/bin/env python3
import pymunk
from pymunk import matplotlib_util

import matplotlib
import matplotlib.pyplot as plt

from pymunk_common import set_circle

class plane_space(pymunk.Space):
    def __init__(self,**keys):
        super().__init__(self)
        for key,value in keys.items():
            setattr(self,key,value)

if __name__ == '__main__':
    WIDTH,HEIGHT = 600,600

    #set munk
    space = plane_space(gravity=(0,-9.8))
    set_circle(space,10,25,(0,0))

    #set plot
    fig = plt.figure()
    ax = plt.axes(xlim=(0,WIDTH),ylim=(0,HEIGHT))
    ax.set_aspect('equal')

    #print image
    output = matplotlib_util.DrawOptions(ax)
    #space.debug_draw(output)
    #plt.show()

    #gen animation
    def init():
        space.debug_draw(output)
    def animate(dt):
        for x in range(10):
            space.step(0.1*x*dt)
        ax.clear()
        space.debug_draw(output)
    from matplotlib import animation
    anim = animation.FuncAnimation(fig,animate,init_func=init,blit=True,frames=100,interval=20)

    #output animation
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15,bitrate=1800)
    anim.save('test.gif',writer=writer)
