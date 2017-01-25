#!/usr/bin/env python3
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(14,10))
ax = plt.axes(xlim=(0,600),ylim=(0,600))
ax.set_aspect('equal')

from pymunk import *
space = Space()
space.gravity = (0,-9.8)
from pymunk_common import set_circle,set_segment
set_circle(space,10,25,(300,200))
set_segment(space,3,(0,50),(500,50))

from pymunk import matplotlib_util
output = matplotlib_util.DrawOptions(ax)
cycle = 80
step = 1e-3
import os
from datetime import datetime
savedir = os.path.expanduser('~/log/matplotlib_test/')+datetime.now().strftime('%Y%m%d_%H%M%S')
os.makedirs(savedir,exist_ok=True)
for i in range(100):
    now = '{0:.2f}'.format(cycle*step*i)
    for j in range(cycle):
        space.step(step)
    ax.clear()
    ax.text(10,10,now,fontsize=12)
    space.debug_draw(output)
    plt.pause(1e-2)
    plt.savefig(savedir+'/'+now+'.jpg')
