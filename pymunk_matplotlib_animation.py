#!/usr/bin/env python3

import matplotlib.pyplot as plt

fig = plt.figure()

from pymunk_common import plane_space
from pymunk.matplotlib_util import DrawOptions
from matplotlib import animation
class anim_space(plane_space):
    def __init__(self,**keys):
        super().__init__(**keys)
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(0,600),ylim=(0,600))
        self.ax.set_aspect('equal')
        self.output = DrawOptions(self.ax)
    def debug_draw(self):
        super().debug_draw(self.output)
    def animate(self,dt):
        for x in range(10):
            space.step(dt*0.1)
        self.ax.clear()
        self.debug_draw()
        return []
    def process(self):
        return animation.FuncAnimation(self.fig,self.animate,frames=20,interval=20,blit=True)

space = anim_space(gravity=(0,-9.8))
space.set_circle(10,10,(300,300))
space.set_segment(10,(0,100),(600,100))
anim = space.process()

anim.save('output.gif',writer='imagemagick')
