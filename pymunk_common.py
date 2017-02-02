def attr_set(obj,keys):
    for key,value in keys.items():
        setattr(obj,key,value)

from pymunk import *
from pymunk.vec2d import Vec2d
class plane_space(Space):
    def __init__(self,**keys):
        super().__init__()
        attr_set(self,keys)
    def set_object(self,body,position,shape,**keys):
        """
        filter:
            group       :number(alias for field number 0)
            categories  :32bit mask(alias for field number 1)
            mask        :32bit mask(alias for field number 2)
        if self.group != other.group: they collide (group 0 collide all other groups)
        if (self.categories & other.mask) != 0: they collide
        """
        body.position = position
        body.start_position = Vec2d(position)
        shape.filter = ShapeFilter(**keys)
        print(shape.filter)
        self.add(body,shape)
    def set_circle(self,mass,radius,position,**keys):
        body = Body(mass,moment_for_circle(mass,0,radius,(0,0)))
        self.set_object(body,position,Circle(body,radius),**keys)
        return body
    def set_segment(self,breadth,*points):
        body = Segment(self.static_body,*points,breadth)
        self.add(body)
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(14,10))
    ax = plt.axes(xlim=(0,600),ylim=(0,600))
    ax.set_aspect('equal')

    space = plane_space(gravity=(0,-9.8))

    space.set_circle(10,25,(300,300),layers=0b0)
    space.set_segment(10,(0,100),(600,100))

    from pymunk.matplotlib_util import DrawOptions
    output = DrawOptions(ax)
    space.debug_draw(output)
    plt.show()
