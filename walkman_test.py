#!/usr/bin/env python3

import pymunk
from pymunk_common import plane_space,set_circle,set_segment
def set_ground(space,breadth,width):
    #set_segment(space,breadth,(0,100),(width,100))
    body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    seg = pymunk.Segment(body,(0,100),(width,100),breadth)
    space.add(seg)

def set_walkman(space,length,x,y):
    set_circle(space,10,10,(x,y))
    set_circle(space,10,10,(x,y+length))


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(14,10))
    ax = plt.axes(xlim=(0,600),ylim=(0,600))
    ax.set_aspect('equal')

    space = plane_space(fig,ax,gravity=(0,-9.8))

    set_walkman(space,100,100,100)
    set_ground(space,1,600)

    import os
    from datetime import datetime
    savedir = os.path.expanduser('~/log/walkman_test/')+datetime.now().strftime('%Y%m%d_%H%M%S')
    os.makedirs(savedir,exist_ok=True)

    cycle,step = 10,1e-2
    for t in range(100):
        now = '{0:.2f}'.format(cycle*step*t)
        for c in range(cycle):
            space.step(step)
        ax.clear()
        ax.text(10,10,now,fontsize=12)
        space.debug_draw(space.output)
        plt.pause(1e-2)
        plt.savefig(savedir+'/'+now+'.jpg')
