class Box():


    def __init__(self, x=0, y=0, w=1, h=1):

        """Accept arguments to define our box, and store them."""

        self.x = x

        self.y = y

        self.w = w

        self.h = h


    def __repr__(self):

        return "Box(%s, %s, %s, %s)" % (self.x, self.y, self.w, self.h)



many_boxes = [Box() for i in range(5000)]