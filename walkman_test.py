import pymunk
from pymunk_common import plane_space

import os
import matplotlib.pyplot as plt
from pymunk.matplotlib_util import DrawOptions
class step_space(plane_space):
    def __init__(self,xlim,ylim,savedir,**keys):
        super().__init__(**keys)
        #set savedir
        os.makedirs(savedir,exist_ok=True)
        self.savedir = savedir
        #set drawoptions
        fig = plt.figure()
        self.ax = plt.axes(xlim=xlim,ylim=ylim)
        self.ax.set_aspect('equal')
        self.output = DrawOptions(self.ax)
        #init
        self.last = 0.
    def step(self,now,division=10,show=True):
        dt = now-self.last
        now_str = '{0:.2f}'.format(now)
        assert division > 0,"division should be >0"
        for d in range(division):
            super().step(dt/division)
        self.ax.clear()
        self.debug_draw(self.output)
        if show:
            plt.pause(step)
        plt.savefig(self.savedir+'/'+now_str+'.jpg')

from pymunk.constraint import PivotJoint
def set_arms(space,weist,y0,num,**filter_keys):
    x,y = weist.position
    step_y = (y - y0)/num
    bodies = [space.set_circle(10,10,(x,y0+step_y*i),**filter_keys) for i in range(num)]
    bodies.append(weist)
    #joints
    joints = [PivotJoint(*bodies[i:i+2],(x+10,y0+step_y*(2*i+1)/2)) for i in range(num)]
    space.add(joints)
def set_walkman(space,x0,y0,length,num,ID=1):
    weist = space.set_circle(10,10,(x0,y0+length),group=ID)
    set_arms(space,weist,y0,num,group=ID)
    set_arms(space,weist,y0,num,group=ID)


if __name__ == '__main__':
    from datetime import datetime
    savedir = os.path.expanduser('~/log/walkman_test')+datetime.now().strftime('%Y%m%d_%H%M%S')
    space = step_space((0,600),(0,600),savedir,gravity=(0,-9.8))

    #set ground
    space.set_segment(10,(0,100),(600,100))

    set_walkman(space,300,200,100,3,ID=1)
    set_walkman(space,300,310,100,3,ID=1)

    step=1e-2
    for t in range(50):
        space.step(step*t,show=True)
