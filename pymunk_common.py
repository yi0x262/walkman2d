from pymunk import *
from pymunk.vec2d import Vec2d

#body
def set_object(space,body,position,shape,elasticity=0.9999):
    body.position = position
    body.start_position = Vec2d(body.position)
    shape.elasticity = elasticity
    space.add(body,shape)
def set_circle(space,mass,radius,position):
    body = Body(mass,
                moment_for_circle(mass,0,radius,(0,0)))
    set_object( space, body, position,
                Circle(body,radius))
    return body
def set_segment(space,breadth,*points):
    body = Segment(space.static_body,*points,breadth)
    space.add(body)
#joint
def set_pivot(body1,body2,**args):
    pass


import matplotlib.pyplot as plt
from matplotlib import animation
def set_animate(space,fig,ax,**keys):
    output = matplotlib_util.DrawOptions(ax)
    def init():
        space.debug_draw(output)
    def animate(dt):
        for x in range(10):
            space.step(0.02)
        ax.clear()
        space.debug_draw(output)
        return list()
    anim = animation.FuncAnimation(fig,animate,init_func=init,**keys)
    return anim

from pymunk import matplotlib_util
class plane_space(Space):
    def __init__(self,fig,ax,**keys):
        super().__init__(self)
        for key,value in keys.items():
            setattr(self,key,value)
        self.output = matplotlib_util.DrawOptions(ax)

if __name__ == '__main__':
    #test
    WIDTH,HEIGHT = 600,600
    space = plane_space(gravity=(0,-9.8))

    set_circle(space,10,25,(300,300))

    set_segment(space,10,(0,100),(WIDTH,100))

    fig = plt.figure()
    ax = plt.axes(xlim=(0,WIDTH),ylim=(0,HEIGHT))
    anim = set_animate(space,fig,ax,frames=100,blit=True,interval=20)
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15,bitrate=1800)
    anim.save('test.gif',writer=writer)
